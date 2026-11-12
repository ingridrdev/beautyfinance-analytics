"""Cria a análise Excel usando os CSVs existentes, sem alterar as fontes."""
import csv
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.series import SeriesLabel
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / 'excel' / 'beautyfinance_analise.xlsx'
MONEY = '"R$" #,##0.00;[Red]-"R$" #,##0.00'
PERCENT = '0.00%;[Red]-0.00%'


def read(path):
    with (ROOT / path).open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def group():
    return [Decimal(0), Decimal(0), set(), 0]


def cents(value):
    return float(value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def format_chart(chart):
    """Define explicitamente eixos e legenda para renderização no Excel."""
    chart.y_axis.title = None
    chart.x_axis.delete = False
    chart.x_axis.axPos = 'b'
    chart.x_axis.tickLblPos = 'nextTo'
    chart.x_axis.tickLblSkip = 1
    chart.x_axis.tickMarkSkip = 1
    chart.y_axis.delete = False
    chart.y_axis.axPos = 'l'
    chart.y_axis.tickLblPos = 'nextTo'
    chart.y_axis.numFmt = '"R$" #,##0'
    chart.y_axis.scaling.min = 0
    chart.legend.position = 'b'
    chart.legend.overlay = False


def main():
    sales = read('data/processed/fato_vendas.csv')
    budget = read('data/raw/fato_orcamento.csv')
    channels = read('data/raw/dim_canais.csv')
    monthly, channel = defaultdict(group), defaultdict(group)
    targets, channel_targets = defaultdict(Decimal), defaultdict(Decimal)
    if max(r['data_venda'] for r in sales)[:7] != '2026-08':
        raise ValueError('Corte mudou: revise a análise fixa de agosto/2026.')
    for row in sales:
        month = row['data_venda'][:7]
        groups = [monthly[month]]
        if month.startswith('2026'):
            groups.append(channel[row['id_canal']])
        for item in groups:
            item[0] += Decimal(row['receita_liquida'])
            item[1] += Decimal(row['custo_total'])
            item[2].add(row['id_pedido'])
            item[3] += int(row['quantidade'])
    for row in budget:
        month = row['mes_referencia'][:7]
        targets[month] += Decimal(row['receita_orcada'])
        if '2026-01' <= month <= '2026-08':
            channel_targets[row['id_canal']] += Decimal(row['receita_orcada'])
    wb = Workbook()
    guide = wb.active
    guide.title = 'Leia-me'
    for row in [
        ['BEAUTYFINANCE ANALYTICS', 'Análise complementar em Excel'],
        ['Dados', 'Empresa e resultados fictícios para estudo e portfólio.'],
        ['Períodos', 'Histórico: 2024 a agosto/2026. Resumo e canais: jan-ago/2026.'],
        ['Orçamento', '2024 a dezembro/2026. Comparável limitado ao último mês realizado.'],
        ['Mensal', 'Meses futuros têm orçamento; realizado e diferenças ficam vazios.'],
        ['Fórmulas', 'Valores de origem em azul; fórmulas em ameixa. Recalcular ao abrir.'],
        ['Pedidos', 'Contagem distinta dos CSVs. Um pedido pode conter vários produtos.'],
        ['Margem', 'Margem bruta não é lucro líquido; percentual usa divisão dos totais.'],
        ['Forecast', 'Receita set-dez/2025 × razão jan-ago/2026 / jan-ago/2025.'],
        ['Limites', 'Total da empresa; sem previsão de custos, margem ou intervalo de incerteza.'],
        ['Metas didáticas', 'Orçamento histórico gerado a partir das vendas, sem independência estatística.'],
        ['Fontes', 'data/processed/fato_vendas.csv; data/raw/fato_orcamento.csv e dim_canais.csv.'],
        ['Atualização', 'Execute src/gerar_analise_excel.py; substitui apenas esta planilha.'],
        ['Conexão', 'Arquivo independente, sem conexão ao Supabase ou ao Power BI.'],
    ]:
        guide.append(row)
    summary = wb.create_sheet('Resumo 2026')
    monthly_sheet = wb.create_sheet('Mensal')
    monthly_sheet.append(['Mês','Ano','Receita','Custo','Margem bruta','Margem %','Pedidos','Unidades','Ticket médio','Orçamento','Comparável','Diferença R$','Diferença %'])
    for month in sorted(targets):
        r = monthly_sheet.max_row + 1
        item = monthly.get(month)
        monthly_sheet.append([month,int(month[:4]),cents(item[0]) if item else None,cents(item[1]) if item else None,
            f'=IF(C{r}="","",C{r}-D{r})',f'=IFERROR(E{r}/C{r},"")',len(item[2]) if item else None,
            item[3] if item else None,f'=IFERROR(C{r}/G{r},"")',cents(targets[month]),
            f'=IF(C{r}="","",J{r})',f'=IF(C{r}="","",C{r}-K{r})',f'=IFERROR(L{r}/K{r},"")'])
    summary.append(['Indicador — janeiro a agosto/2026','Valor'])
    for label, value in [
        ('Receita líquida','=SUMIF(Mensal!B2:B37,2026,Mensal!C2:C37)'),
        ('Custo total','=SUMIF(Mensal!B2:B37,2026,Mensal!D2:D37)'),
        ('Margem bruta','=B2-B3'),('Margem percentual','=IFERROR(B4/B2,"")'),
        ('Pedidos distintos',len(set().union(*(v[2] for k,v in monthly.items() if k.startswith('2026'))))),
        ('Unidades',sum(v[3] for k,v in monthly.items() if k.startswith('2026'))),
        ('Ticket médio','=IFERROR(B2/B6,"")'),
        ('Orçamento comparável','=SUMIF(Mensal!B2:B37,2026,Mensal!K2:K37)'),
        ('Diferença R$','=B2-B9'),('Diferença %','=IFERROR(B10/B9,"")')]:
        summary.append([label,value])
    cs = wb.create_sheet('Canais 2026')
    cs.append(['Canal','Receita','Custo','Margem bruta','Margem %','Pedidos','Unidades','Ticket médio','Orçamento comparável','Diferença R$','Diferença %'])
    for ch in sorted(channels,key=lambda x: channel[x['id_canal']][0],reverse=True):
        r = cs.max_row + 1
        v = channel[ch['id_canal']]
        cs.append([ch['nome_canal'],cents(v[0]),cents(v[1]),f'=B{r}-C{r}',f'=IFERROR(D{r}/B{r},"")',len(v[2]),v[3],
            f'=IFERROR(B{r}/F{r},"")',cents(channel_targets[ch['id_canal']]),f'=B{r}-I{r}',f'=IFERROR(J{r}/I{r},"")'])
    fs = wb.create_sheet('Forecast')
    base25 = sum(v[0] for k,v in monthly.items() if '2025-01' <= k <= '2025-08')
    base26 = sum(v[0] for k,v in monthly.items() if '2026-01' <= k <= '2026-08')
    for row in [['Base comparável','Receita'],['Jan-ago/2025',cents(base25)],['Jan-ago/2026',cents(base26)],
        ['Fator sem arredondar','=B3/B2'],['Crescimento','=B4-1'],[],
        ['Mês','Receita base 2025','Previsão','Orçamento','Diferença R$','Diferença %']]:
        fs.append(row)
    for m in range(9,13):
        r = fs.max_row+1
        fs.append([f'2026-{m:02}',cents(monthly[f'2025-{m:02}'][0]),f'=ROUND(B{r}*$B$4,2)',cents(targets[f'2026-{m:02}']),f'=C{r}-D{r}',f'=IFERROR(E{r}/D{r},"")'])
    fs.append(['Total','=SUM(B8:B11)','=SUM(C8:C11)','=SUM(D8:D11)','=C12-D12','=IFERROR(E12/D12,"")'])
    for sheet, cols, pct, start, end in [(monthly_sheet,[3,4,5,9,10,11,12],[6,13],2,37),(cs,[2,3,4,8,9,10],[5,11],2,6),(fs,[2,3,4,5],[6],8,12)]:
        for r in range(start,end+1):
            for c in cols: sheet.cell(r,c).number_format=MONEY
            for c in pct: sheet.cell(r,c).number_format=PERCENT
    for r in range(2,12): summary.cell(r,2).number_format=PERCENT if r in (5,11) else ('#,##0' if r in (6,7) else MONEY)
    fs['B2'].number_format=fs['B3'].number_format=MONEY
    fs['B4'].number_format='0.0000000000'
    fs['B5'].number_format=PERCENT
    for sheet, ref, name in [(monthly_sheet,'A1:M37','TabelaMensal'),(cs,'A1:K6','TabelaCanais'),(fs,'A7:F11','TabelaForecast')]:
        table=Table(displayName=name,ref=ref)
        table.tableStyleInfo=TableStyleInfo(name='TableStyleMedium4',showRowStripes=True)
        sheet.add_table(table)
    for sheet in wb:
        sheet.sheet_view.showGridLines=False
        sheet.freeze_panes='B8' if sheet==fs else 'B2'
        sheet.page_setup.orientation='landscape'
        sheet.page_setup.paperSize=sheet.PAPERSIZE_A4
        sheet.sheet_properties.pageSetUpPr.fitToPage=True
        sheet.page_setup.fitToWidth=1
        sheet.page_setup.fitToHeight=0
        for row in sheet:
            for cell in row:
                cell.font=Font(name='Calibri',size=11,color='632D4B' if cell.data_type=='f' else '245A81')
                cell.alignment=Alignment(vertical='center')
        for r in ([1,7] if sheet==fs else [1]):
            sheet.row_dimensions[r].height=32
            for cell in sheet[r]:
                cell.fill=PatternFill('solid',fgColor='632D4B')
                cell.font=Font(name='Calibri',size=11,bold=True,color='FFFFFF')
        for col in sheet.columns: sheet.column_dimensions[col[0].column_letter].width=23
        sheet.column_dimensions['A'].width=33
    guide.column_dimensions['B'].width=100
    for row in guide:
        guide.row_dimensions[row[0].row].height=36
        row[1].alignment=Alignment(wrap_text=True,vertical='center')
    summary.column_dimensions['A'].width=46
    for sheet, ref in [(monthly_sheet,'L2:M37'),(cs,'J2:K6'),(fs,'E8:F12')]:
        for op,color in [('lessThan','B13846'),('greaterThan','196D54')]:
            sheet.conditional_formatting.add(ref,CellIsRule(operator=op,formula=['0'],font=Font(color=color)))
    for sheet,source,title,cols,first,last,anchor in [
        (summary,monthly_sheet,'Receita e orçamento comparável — 2026',[3,11],26,33,'D2'),
        (cs,cs,'Realizado e orçamento por canal — 2026',[2,9],2,6,'A10'),
        (fs,fs,'Previsão e orçamento — set-dez/2026',[3,4],8,11,'A15')]:
        chart=BarChart()
        chart.title=title
        chart.y_axis.title='Receita (R$)'
        chart.grouping='clustered'
        chart.overlap=0
        for col in cols: chart.add_data(Reference(source,min_col=col,min_row=first,max_row=last))
        chart.set_categories(Reference(source,min_col=1,min_row=first,max_row=last))
        for series,label,color in zip(chart.series,['Previsão' if sheet==fs else 'Realizado','Orçamento'],['632D4B','B6AAA2']):
            series.tx=SeriesLabel(v=label)
            series.graphicalProperties.solidFill=color
            series.graphicalProperties.line.solidFill=color
        chart.width,chart.height=24,12
        format_chart(chart)
        sheet.add_chart(chart,anchor)
    OUTPUT.parent.mkdir(exist_ok=True)
    wb.save(OUTPUT)
    check=load_workbook(OUTPUT)
    assert check.sheetnames==['Leia-me','Resumo 2026','Mensal','Canais 2026','Forecast']
    assert base26==Decimal('497957.18')
    assert sum(channel_targets.values())==Decimal('479918.23')
    forecasts=[cents(monthly[f'2025-{m:02}'][0]*base26/base25) for m in range(9,13)]
    assert forecasts==[63645.73,64403.80,90927.21,98709.50]
    print(f'Criado: {OUTPUT}')
    print('Referências CSV conferidas; recalcular fórmulas no Excel.')


if __name__=='__main__':
    main()
