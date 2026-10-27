# Canais e Regiões — primeira versão

Implementada e conferida no Power BI Desktop em 20/10/2026. As capturas
confirmaram a página inicial e os filtros combinados E-commerce + Sudeste.
Os seis cenários DAX coincidiram com as referências de receita, custo,
margem, percentual, pedidos, unidades e ticket médio. A usuária salvou e
fechou o Desktop. Registrada e enviada ao GitHub no commit 58ac9b8.
Para a revisão das cinco páginas, consultar docs/revisao_dashboard_powerbi.md.

## Conteúdo e regras

A terceira página compara receita e margem percentual por canal e por região
em quatro gráficos de barras. Os seis cartões mostram receita líquida,
margem bruta, margem percentual, pedidos, unidades vendidas e ticket médio.
Os detalhes das barras incluem também o custo total.

Cinco filtros: ano, meses, marca, canal e região. O estado inicial é 2026,
sem seleções adicionais, com corte fixo do realizado até 31/08/2026.
Os anos históricos 2024 e 2025 permanecem disponíveis. Não há forecast aqui.

A receita e a margem percentual têm rankings separados, pois o canal ou
região com maior receita pode não ter a maior margem. A margem percentual
divide a margem total pela receita total de cada grupo, sem média simples.
O ticket médio divide a receita pelos pedidos distintos do recorte.
Não somar tickets nem percentuais entre canais/regiões.

Clicar em uma barra foi configurado para filtrar os demais gráficos e cartões.
Os gráficos não restringem os filtros do topo. Ano restringe a lista de meses.
Ao trocar o ano, limpe meses incompatíveis. Canal e região podem ser combinados.

## Validação local

- 21 JSONs (19 visuais, página e ordem das páginas) passaram nos schemas
  oficiais da Microsoft previamente consultados, sem instalar dependências.
- Referências a campos e medidas, nomes únicos, interações e posições
  dentro da página foram conferidas; não há sobreposição dos elementos.
- Receita, custo, unidades e conjunto de pedidos foram conferidos contra
  os grupos por canal e região com leitura sequencial dos CSVs.
- Dinheiro calculado com Decimal, sem gerar ou alterar dados.
- Consulta 1 e validar_canais_regioes.dax são idênticos.
- Nenhuma medida, relação, fonte ou tabela foi alterada. As duas páginas
  anteriores permanecem preservadas. Mudaram apenas a ordem/aba ativa e a
  consulta salva. O teste anterior continua em validar_produtos_marcas.dax.

O teste DAX foi executado e os seis cenários conferem, incluindo o recorte
E-commerce + Sudeste em agosto/2026. Margens como fração e tickets com mais
casas coincidem com os arredondamentos dos cartões. A captura dos filtros
combinados confirmou também os seis cartões: receita 61.148,54, margem
35.447,50, percentual 57,97%, 486 pedidos, 996 unidades e ticket 125,82.
Não foram apresentados cliques nas barras, filtros de outros anos ou uma
captura do recorte de agosto; não considerar essas interações comprovadas.

## Conferência no Desktop

1. Reabra powerbi/beauty_analytics.pbip, clique em Atualizar e abra Canais e Regiões.
2. Envie uma captura inicial. Confira os cartões com a linha Jan-ago 2026 abaixo.
3. Selecione E-commerce em Canal e Sudeste em Região. Confira a linha combinada.
4. Mantendo os dois filtros, selecione 2026-08 em Meses. Confira a última linha.
5. Na Exibição de consulta DAX, execute Consulta 1 e envie as seis linhas.
   O código já está pronto; a margem vem como fração e o ticket com mais casas.
6. Selecione uma barra de canal e confira se cartões e gráficos por região mudam.
   Limpe a seleção e teste uma barra de região. Esses cliques precisam da interface.
7. Restaure Ano 2026 e demais filtros em Todos. Salve com Ctrl + S.
   Mantenha o Desktop aberto durante a revisão e feche antes de novas edições externas.

| Cenário | Receita | Custo | Margem bruta | Margem % (0 a 100) | Pedidos | Unidades | Ticket médio |
|---|---:|---:|---:|---:|---:|---:|---:|
| Jan-ago 2026 | 497957.18 | 206597.98 | 291359.20 | 58.51 | 3872 | 7939 | 128.60 |
| E-commerce 2026 | 136179.09 | 57283.99 | 78895.10 | 57.93 | 1093 | 2215 | 124.59 |
| Sudeste 2026 | 228887.49 | 94864.46 | 134023.03 | 58.55 | 1757 | 3662 | 130.27 |
| E-commerce Sudeste 2026 | 61148.54 | 25701.04 | 35447.50 | 57.97 | 486 | 996 | 125.82 |
| Agosto 2026 | 59569.39 | 24968.26 | 34601.13 | 58.09 | 492 | 945 | 121.08 |
| E-commerce Sudeste agosto 2026 | 6498.81 | 2811.68 | 3687.13 | 56.74 | 59 | 105 | 110.15 |

## Arquivos e registro

Arquivos desta tarefa: pasta bf_canais_regioes com page.json e 19 visual.json,
pages.json, Consulta 1.dax, powerbi/validar_canais_regioes.dax e este documento.
Revisar os arquivos adicionais que o Desktop gerar ao salvar antes de incluí-los.
O documento local de progresso continua ignorado; .gitignore permanece separado.

Nenhuma ação necessária no Supabase. Após conferir no Desktop, salvar,
fechar e revisar os arquivos antes de registrar no GitHub.
Mensagem sugerida: feat: add channels and regions analysis page
Registro original concluído no commit 58ac9b8. Novos registros exigem
autorização específica da usuária.

Referência: [PBIR — Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report).
