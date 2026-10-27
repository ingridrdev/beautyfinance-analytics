# Relacionamentos do modelo Power BI

Atualizado em 20/10/2026. As nove relações foram conferidas no Desktop e
os 13 resultados da consulta original coincidiram com as referências.
O calendário, as medidas e as cinco páginas foram implementados depois.
Este guia descreve o modelo atual; não é necessário recriar as relações
ou refazer a validação original apenas para continuar o projeto.

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
produto, canal ou região. A relação não transmite esses filtros ao forecast.
Para evitar exibir o total da empresa como se fosse uma previsão detalhada,
as quatro medidas de forecast retornam vazio se houver filtro direto em
dim_produtos, dim_canais ou dim_regioes. Isso inclui marca e categoria.
Os testes DAX confirmaram os retornos vazios para marca, canal e região.
A página Forecast já está construída e oferece somente o filtro mensal.
Usar suas medidas nos visuais; a proteção não se aplica a somas diretas
das colunas de previsão.

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

Os testes locais não executam o motor do Power BI. Depois deles, a usuária
apresentou no Desktop as nove relações ativas e os 13 resultados DAX abaixo;
todos coincidiram com as referências. Também confirmou a carga das sete
tabelas. O teste foi preservado em powerbi/validar_relacionamentos.dax.

O calendário já foi configurado como tabela de datas, com data como chave
e mes_nome ordenado por mes_numero. O teste do Desktop confirmou 1.096
datas distintas e contínuas, 36 meses e o dia bissexto de 2024. As medidas
mensais e anuais usam esse calendário; consultar os guias específicos.
O modelo atual possui 21 medidas. Nenhuma relação foi alterada nesta atualização.

## Como repetir a conferência, se o modelo mudar

O procedimento abaixo é uma referência para mudanças futuras. A Consulta 1
salva é usada para o teste da tarefa atual; não pressupor que ela ainda
contenha o teste de relacionamentos.

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

Referências coincidentes com a saída original do Desktop, não comandos:

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

## Estado atual e registro

As cinco páginas são Visão Executiva, Produtos e Marcas, Canais e Regiões,
Orçamento x Realizado e Forecast. As quatro primeiras limitam o realizado
até agosto/2026; Forecast usa setembro-dezembro/2026. As tabelas de fatos
compartilham dimensões, com cada gráfico usando medidas do período correto.

Consultar docs/revisao_dashboard_powerbi.md para a revisão em andamento,
evidências e limitações. Conferir arquivos não substitui testar interações.

Nenhuma ação necessária no Supabase. A atualização deste guia é documental,
sem mudança em relationships.tmdl, medidas ou banco. Não recriar relações
nem repetir o commit original para registrar este texto.

Após revisar a tarefa atual, incluir este guia junto dos arquivos efetivamente
alterados na revisão. Não incluir outras pendências automaticamente.
continuidade_projeto.md permanece local e ignorado. cache.abf e
localSettings.json também não devem entrar no GitHub.
