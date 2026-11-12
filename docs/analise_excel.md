# Análise complementar em Excel

Arquivo: [beautyfinance_analise.xlsx](../excel/beautyfinance_analise.xlsx).

## Conteúdo

- **Leia-me:** fontes, períodos, regras e limites.
- **Resumo 2026:** receita, custos, margem, pedidos, unidades, ticket e orçamento comparável de janeiro a agosto; gráfico mensal.
- **Mensal:** 36 meses, com histórico realizado, orçamento e diferenças calculadas por fórmulas. Setembro a dezembro/2026 mantêm realizado e diferenças vazios.
- **Canais 2026:** comparação por canal, margens, pedidos e ticket; gráfico de realizado e orçamento.
- **Forecast:** bases comparáveis, fator sem arredondamento intermediário e previsão dos quatro meses finais, com gráfico.

Valores de origem aparecem em azul e fórmulas em ameixa. Os gráficos e
fórmulas usam as células da planilha. Não há conexão externa nem alteração
dos dados de origem. Os pedidos são contados como distintos no gerador;
o resumo não soma contagens de produtos.

O orçamento histórico é didático e foi gerado a partir das vendas. A margem
bruta não representa lucro líquido. O forecast é total da empresa, sem
projeção de custos ou intervalo de incerteza. O corte é agosto/2026.

## Reprodução

Com as dependências de requirements.txt instaladas, execute na raiz:

```powershell
.\.venv\Scripts\python.exe src/gerar_analise_excel.py
```

O comando substitui somente excel/beautyfinance_analise.xlsx. Feche a
planilha antes de recriá-la. Abra no Excel para recalcular as fórmulas e
salve: o openpyxl grava fórmulas, mas não as executa. A planilha entregue
nesta etapa foi recalculada e salva pelo Excel instalado.

## Conferência visual

Abra Resumo 2026 e confira receita de R$ 497.957,18, margem de 58,51%,
orçamento de R$ 479.918,23 e diferença de R$ 18.038,95 (3,76%). Em Forecast,
confira R$ 317.686,24 previsto e diferença de -R$ 21.648,49 (-6,38%).
Em Canais 2026, Supermercados deve apresentar -R$ 3.679,82 (-4,80%).

A captura da usuária confirmou a abertura da planilha e os indicadores do
Resumo 2026. Após o primeiro ajuste, os meses, valores monetários do eixo
e legenda inferior ficaram visíveis. A captura revelou sobreposição do
título vertical; esse título foi removido dos três gráficos. O Excel
recalculou e salvou o arquivo, sem erros de fórmula e com totais preservados.
A captura final confirmou Resumo 2026 sem sobreposição, com indicadores,
meses e legenda legíveis. A usuária confirmou por texto a conferência das
abas Canais 2026 e Forecast e o fechamento do Excel. Essas duas abas não
tiveram capturas recebidas nesta revisão. Conferência concluída em 12/11/2026.
