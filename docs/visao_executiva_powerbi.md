# Visão Executiva — primeira versão

Implementada em 15/10/2026. Conferência no Desktop em 20/10/2026:
a página abriu e os oito indicadores iniciais coincidiram com as referências.
A usuária confirmou os testes de agosto/2026 e E-commerce em agosto/2026,
salvou e fechou o Power BI. O resultado da consulta DAX de três linhas e os
demais testes de interação abaixo não foram apresentados nesta revisão.

## O que foi construído

A antiga Página 1 foi renomeada para Visão Executiva. O tamanho de
1920 por 1080 e o vínculo com o modelo existente foram preservados.

- Cabeçalho, identificação de dados fictícios e corte do realizado.
- Cinco filtros: ano, meses, marca, canal e região.
- Seis cartões: receita líquida, custo total, margem bruta, margem
  percentual, pedidos e ticket médio.
- Colunas agrupadas de realizado e orçamento comparável por mês.
- Linha de margem percentual por mês.
- Barras de receita por região, em ordem decrescente.
- Dois cartões auxiliares de diferença contra orçamento, em reais e percentual.
- Detalhes mensais com unidades, MoM e YoY no gráfico de receita.

São 20 elementos: oito cartões, três gráficos, cinco filtros e quatro
caixas de texto. Usam visuais nativos, com fundo claro, cartões brancos e
cores ameixa/cinza para realizado e orçamento. As diferenças têm sinal
positivo/negativo e cor condicional verde/vermelha.

## Estado inicial e limites

O filtro de ano tem seleção inicial 2026. Os meses começam sem restrição
adicional. O filtro fixo da página limita as datas a 31/08/2026, deixando
disponível todo o histórico de 2024/2025 e janeiro-agosto de 2026.

O ano pode ser alterado; a seleção de meses deve ser limpa quando ficar
incompatível com outro ano. O orçamento usado nos visuais é o comparável.
MoM e YoY aparecem nos detalhes mensais, sem transformar o total de vários
meses em uma taxa mensal. A previsão ficará em sua própria página futura.

Seleções nos gráficos foram configuradas para filtrar os indicadores;
os gráficos não devem limitar as opções dos segmentadores. O filtro de
ano pode filtrar a lista de meses. Essas interações ainda precisam de
conferência dentro do Desktop.

Nenhuma medida, relação, tabela, fonte ou credencial foi alterada. Não
foram criadas outras páginas. A consulta salva foi atualizada apenas para
facilitar o teste dos indicadores da página.

## Validação local realizada

- Página e 20 arquivos visual.json validados com jsonschema contra os
  schemas oficiais da Microsoft, incluindo suas referências.
- Seleção inicial do ano, corte da página, interações e ordenações conferidos.
- Medidas e colunas usadas pelos visuais existem no modelo.
- Elementos com nomes únicos, dentro da página e sem sobreposições geométricas.
- Indicadores iniciais e dois recortes recalculados dos CSVs com Decimal.
- Soma das regiões no estado inicial coincide com a receita total.
- Consulta 1 idêntica ao teste powerbi/validar_visao_executiva.dax.

Nenhuma dependência foi instalada. Os schemas foram consultados e mantidos
em cache temporário, fora do repositório. A validação de schema verifica
a estrutura dos arquivos; não comprova que cada propriedade de formatação
será renderizada como desejado no Desktop.

Referência: [Formato PBIR e arquivos de relatório](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report).

## Reabrir e conferir

1. Reabra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Abra a exibição Relatório e a página Visão Executiva.
3. Confira se o ano está em 2026 e os filtros de marca/canal/região sem restrição.
4. Envie uma captura da página inteira. Se aparecer erro de abertura ou
   visual, envie o texto antes de fazer commit. Não descartar trabalho.
5. Confira os números iniciais abaixo, os títulos e a legibilidade.
6. Na Exibição de consulta DAX → Consulta 1, clique em Executar e envie
   as três linhas. O teste já foi colocado, sem necessidade de copiar código.
7. Na página, selecione agosto e depois canal E-commerce, para conferir
   os filtros com as referências da tabela. Limpe essas seleções ao terminar.
8. Passe o mouse sobre agosto: MoM da empresa 4,83% e YoY 0,80%.
   Com E-commerce selecionado: MoM 10,36% e YoY -7,66%.
9. Teste uma região e confira se os indicadores mudam. Limpe a seleção
   clicando novamente na barra selecionada ou em uma área vazia do gráfico.
10. Teste o ano 2025, com meses sem restrição, e confira se aparecem os
    doze meses em ordem. Volte ao ano 2026 antes de salvar o estado inicial.
11. Após aprovação, salve com Ctrl + S. Feche antes de futuras edições
    externas e reabra para testar, conforme orientação.

Resultados esperados:

| Indicador | Inicial jan-ago/2026 | Agosto/2026 | E-commerce em agosto/2026 |
|---|---:|---:|---:|
| Receita líquida | 497.957,18 | 59.569,39 | 15.262,98 |
| Custo total | 206.597,98 | 24.968,26 | 6.480,71 |
| Margem bruta | 291.359,20 | 34.601,13 | 8.782,27 |
| Margem percentual | 58,51% | 58,09% | 57,54% |
| Pedidos | 3.872 | 492 | 136 |
| Ticket médio | 128,60 | 121,08 | 112,23 |
| Orçamento comparável | 479.918,23 | 57.792,52 | 13.765,14 |
| Variação em reais | 18.038,95 | 1.776,87 | 1.497,84 |
| Variação percentual | 3,76% | 3,07% | 10,88% |

As consultas DAX conferem medidas em recortes definidos, mas não substituem
o teste dos filtros e interações dos visuais. A comparação do ano 2026
inclui somente os oito meses realizados e não a previsão de fim de ano.

## Registrar após a revisão

Nenhuma ação no Supabase. No Source Control, revisar e preparar pelo +:

- beauty_analytics.Report/definition/pages/872e11e20f82508151af/page.json.
- Os 20 visual.json da pasta visuals dessa página.
- beauty_analytics.SemanticModel/DAXQueries/Consulta 1.dax.
- powerbi/validar_visao_executiva.dax.
- docs/visao_executiva_powerbi.md.
- docs/visao_executiva_planejamento.md, cujo estado foi atualizado.
- beauty_analytics.SemanticModel/definition/cultures/pt-BR.tmdl: nomes
  auxiliares dos campos gerados pelo Desktop ao salvar, sem mudar cálculos.

Os arquivos adicionais que o Desktop gerar ao salvar devem ser revisados
separadamente. Não incluir cache.abf, localSettings.json ou outras pendências.
O documento de progresso continua local e ignorado.

Mensagem: `feat: build executive overview page`.
Clique em Commit e depois ... → Push manualmente, após a conferência.
Não construir outras páginas antes da revisão desta primeira versão.
