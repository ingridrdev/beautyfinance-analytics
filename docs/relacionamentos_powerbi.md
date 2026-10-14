# Relacionamentos do modelo Power BI

## O que foi configurado

Nove relacionamentos ativos, com filtro em uma direção. Cada código ou
data aparece uma vez na dimensão e pode aparecer muitas vezes nas tabelas
de valores. Por isso, os relacionamentos são de um para muitos (1:*).

| Dimensão, lado 1 | Tabela de valores, lado * |
|---|---|
| dim_produtos.id_produto | fato_vendas.id_produto |
| dim_canais.id_canal | fato_vendas.id_canal |
| dim_regioes.id_regiao | fato_vendas.id_regiao |
| dim_calendario.data | fato_vendas.data_venda |
| dim_produtos.id_produto | fato_orcamento.id_produto |
| dim_canais.id_canal | fato_orcamento.id_canal |
| dim_regioes.id_regiao | fato_orcamento.id_regiao |
| dim_calendario.data | fato_orcamento.mes_referencia |
| dim_calendario.data | vw_forecast_receita.mes_referencia |

O filtro vai da dimensão para os valores. Por exemplo, escolher um canal
em dim_canais filtra suas vendas e seu orçamento. Vendas e orçamento não
foram ligados diretamente, evitando caminhos adicionais de filtro.

O forecast só tem relação com o calendário, pois não é dividido por
produto, canal ou região. Esses filtros não alteram a previsão total.
Isso precisa ficar claro na futura página de forecast.

Fonte técnica: [Relacionamentos no modelo tabular](https://learn.microsoft.com/en-us/analysis-services/tmsl/relationships-object-tmsl).

## Datas mensais

O Power Query acrescenta mes_referencia à tabela importada do forecast.
Ela converte ano_mes_forecast, como 2026-09, em 01/09/2026.
Nenhuma coluna foi adicionada ao banco; as receitas previstas não mudaram.

Orçamento e previsão são mensais, representados pelo primeiro dia do mês.
Use ano, trimestre e ano_mes de dim_calendario nas comparações. Um filtro
por um dia que não seja o primeiro não representa uma distribuição diária
do orçamento ou da previsão. Não há rateio diário nesta etapa.

## Validação local realizada

- Nove ligações únicas, com colunas e tipos compatíveis no modelo.
- Chaves das quatro dimensões sem vazios ou duplicidades nos CSVs.
- Todas as chaves das vendas e do orçamento existem nas dimensões.
- Calendário com 1.096 datas consecutivas e cobertura dos quatro meses previstos.
- Totais e recortes dos CSVs calculados com Decimal para referência.

Esses testes não executam o motor do Power BI. A leitura dos arquivos TMDL,
a consulta M e os filtros DAX ainda devem ser confirmados no Desktop.
Não foram criadas medidas financeiras nesta etapa. A marcação formal da
tabela de datas e medidas de tempo será tratada na etapa correspondente.

## Conferir no Power BI Desktop

1. Abra beauty_analytics.pbip e clique em **Atualizar**.
2. Na **Exibição de modelo** (ícone de tabelas ligadas à esquerda), confira
   as nove linhas: lado 1 nas dimensões, lado * nos valores e filtro único.
3. O forecast deve estar ligado somente ao calendário. Não criar relações
   adicionais automaticamente para tentar conectá-lo às outras dimensões.
4. Abra a **Exibição de consulta DAX**, pelo ícone DAX à esquerda.
5. Cole todo o conteúdo de `powerbi/validar_relacionamentos.dax` na consulta
   e clique em **Executar**. Não cole no campo de criação de medida.
6. Compare o resultado com a tabela abaixo. Envie erro ou diferença antes
   de registrar esta etapa como validada. Se estiver certo, salve o projeto.

Resultados esperados, não comandos:

| Resultado da consulta | Valor |
|---|---:|
| Linhas de vendas | 22.734 |
| Linhas de orçamento | 9.828 |
| Linhas de forecast | 4 |
| Receita total | 1.975.524,68 |
| Receita produto 1 | 154.776,97 |
| Orçamento produto 1 | 175.146,30 |
| Receita canal 1 | 545.089,65 |
| Orçamento canal 1 | 582.170,03 |
| Receita região 1 | 133.299,01 |
| Orçamento região 1 | 167.010,19 |
| Receita agosto 2026 | 59.569,39 |
| Orçamento agosto 2026 | 57.792,52 |
| Forecast setembro 2026 | 63.645,73 |

As referências de orçamento por produto/canal/região incluem todo o
orçamento até dezembro de 2026. Não compará-las com o orçamento limitado
ao realizado até agosto. O teste de cada filtro usa a dimensão, para
verificar que a relação realmente transmite o filtro.

## Supabase e GitHub

Não é necessário executar SQL no Supabase para esta tarefa.

Depois da conferência no Power BI, revise as diferenças no Source Control
do VS Code. Prepare somente os arquivos desta tarefa pelo botão +:

- relationships.tmdl.
- tables/vw_forecast_receita.tmdl.
- powerbi/validar_relacionamentos.dax.
- docs/relacionamentos_powerbi.md.
- Eventuais arquivos de definição que o Desktop atualizar ao salvar,
  depois de revisar seu conteúdo.

Não incluir automaticamente outras pendências. O documento local
continuidade_projeto.md permanece ignorado. Não incluir cache.abf ou
localSettings.json.

Mensagem sugerida: `feat: define Power BI model relationships`.
Clique em Commit e depois no menu ... → Push. Aguarde a revisão antes
de avançar para medidas.
