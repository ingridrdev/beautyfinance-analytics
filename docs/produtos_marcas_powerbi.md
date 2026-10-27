# Produtos e Marcas — primeira versão

Implementada e conferida no Power BI Desktop em 20/10/2026. A captura
confirmou a abertura, os seis cartões iniciais e os rankings. A usuária
confirmou os filtros de Produto 1 e Produto 1 em agosto/2026 e apresentou
os seis cenários DAX: todos coincidiram com as referências abaixo.
Salvou e fechou o Desktop. Registrada e enviada ao GitHub no commit 96f8942.
Para a revisão das cinco páginas, consultar docs/revisao_dashboard_powerbi.md.

## Conteúdo

A segunda página segue a identidade visual da Visão Executiva. Tem cinco
filtros (ano, meses, marca, categoria e produto), seis cartões e três gráficos:
receita por produto, receita por marca e margem percentual por categoria.
Todos os 15 produtos participam do ranking, sem filtro de top N.

Os cartões mostram receita líquida, custo total, margem bruta, margem
percentual, unidades vendidas e ticket médio. Os detalhes das barras trazem
os demais indicadores para comparar volume e rentabilidade.
A margem percentual é a divisão dos totais, sem média simples das margens.
Ticket médio por produto considera os pedidos que contêm o produto; não
deve ser somado entre produtos, pois um pedido pode conter vários produtos.

O estado inicial é 2026 sem filtros adicionais, com corte até 31/08/2026.
Os anos de 2024 e 2025 continuam disponíveis. Não há forecast nesta página.
Clicar nas barras filtra gráficos e cartões, sem restringir os filtros do topo.
Marca e categoria restringem a lista de produtos; ao trocar uma seleção,
limpe o produto anterior se ficar incompatível.

## Validações e limites

Os 20 arquivos JSON (página, ordem das páginas e 18 visuais) passaram nos
schemas oficiais da Microsoft. Os gráficos usam o schema publicado 2.7;
o 2.14 indicado pelo Desktop no visual de origem retornou 404 na consulta.
O teste DAX avulso e a Consulta 1 são idênticos. A Visão Executiva não mudou.

Foram conferidos os campos e medidas referenciados, nomes únicos, posições
dentro da página e ausência de sobreposição dos 18 elementos. Os valores
foram calculados por leitura sequencial do CSV, com Decimal para dinheiro,
sem executar os scripts de geração e sem modificar os dados.
As somas por produto, marca e categoria coincidem com o total da receita,
do custo e das unidades. Pedidos distintos não são somáveis entre produtos.

Nenhuma medida, relação, tabela ou fonte foi alterada. A Visão Executiva
foi preservada; somente a ordem/aba ativa foi atualizada para abrir a nova página.
A consulta salva foi substituída pelo teste desta tarefa. O teste anterior
permanece em powerbi/validar_visao_executiva.dax.

## Conferência no Desktop

1. Abra powerbi/beauty_analytics.pbip, clique em Atualizar e abra Produtos e Marcas.
2. Envie uma captura inicial; confira os seis cartões com a primeira linha abaixo.
3. Selecione Gel de Limpeza Facial no filtro Produto e confira a segunda linha.
4. Selecione agosto mantendo esse produto: confira a última linha.
5. Limpe Produto e Meses. Teste Marca Lumera e depois, limpando Marca,
   Categoria Cuidados com a Pele. Os valores esperados estão abaixo.
6. Para conferir todos os seis cenários juntos, abra a Exibição de consulta DAX,
   execute Consulta 1 e envie o resultado. Não precisa copiar o código.
7. Confira se clicar em uma barra filtra os cartões e os outros gráficos.
8. Restaure 2026 e os demais filtros em Todos. Salve com Ctrl + S.
   Mantenha aberto durante a revisão; feche antes de futuras edições externas.

A consulta DAX confirmou as medidas nos seis recortes. A margem saiu como
fração (0,585108... = 58,51%) e o ticket com mais casas, compatíveis com o
arredondamento dos cartões. A captura confirmou a aparência inicial e os
filtros de produto/mês foram confirmados pela usuária. Interações por clique
nas barras e os demais anos não foram apresentados nesta revisão.

| Cenário | Receita | Custo | Margem bruta | Margem % (0 a 100) | Unidades | Ticket médio |
|---|---:|---:|---:|---:|---:|---:|
| Jan-ago 2026 | 497957.18 | 206597.98 | 291359.20 | 58.51 | 7939 | 128.60 |
| Produto 1 | 39272.86 | 16524.05 | 22748.81 | 57.93 | 608 | 88.25 |
| Marca Lumera | 124171.45 | 51933.44 | 72238.01 | 58.18 | 1693 | 108.73 |
| Categoria Cuidados com a Pele | 167722.91 | 70120.54 | 97602.37 | 58.19 | 2221 | 115.43 |
| Agosto 2026 | 59569.39 | 24968.26 | 34601.13 | 58.09 | 945 | 121.08 |
| Produto 1 agosto 2026 | 4616.29 | 1958.59 | 2657.70 | 57.57 | 71 | 88.77 |

## GitHub e Supabase

Nenhuma ação necessária no Supabase. Após a revisão e validação no Desktop,
salvar e fechar o Power BI antes de conferir os arquivos que ele gerar.

Arquivos da tarefa: nova pasta de página bf_produtos_marcas (page.json e
18 visual.json), pages.json, validar_produtos_marcas.dax, Consulta 1.dax e
este documento. Incluir também cultures/pt-BR.tmdl: o Desktop acrescentou
nomes auxiliares Categoria e Produto, sem mudar cálculos.
O documento local de progresso continua ignorado. Não incluir
a pendência de .gitignore automaticamente.

Mensagem sugerida: feat: add products and brands analysis page

O commit e o push ficam sob controle da usuária. A autorização específica
para enviar a Visão Executiva não é autorização permanente para outras etapas.

Referência do formato: [PBIR — Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report).
