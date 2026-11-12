# Dicionário de Dados

Este documento descreve as tabelas e colunas utilizadas no projeto BeautyFinance Analytics.

## Conceitos importantes

- Chave primária: código único que identifica cada registro.
- Chave estrangeira: código utilizado para conectar uma tabela a outra.
- Dimensão: tabela que descreve produtos, canais, regiões ou datas.
- Fato: tabela que armazena valores que serão analisados, como vendas e orçamento.

---

## Tabela: dim_produtos

Armazena as informações dos produtos.

| Coluna | Tipo | Descrição |
|---|---|---|
| id_produto | Número inteiro | Código único do produto |
| nome_produto | Texto | Nome do produto |
| marca | Texto | Marca fictícia do produto |
| categoria | Texto | Categoria do produto |
| preco_sugerido | Número decimal | Preço sugerido de venda |
| custo_base | Número decimal | Custo inicial do produto |
| data_lancamento | Data | Data de lançamento |
| status_produto | Texto | Indica se o produto está ativo ou inativo |

---

## Tabela: dim_canais

Armazena os canais de venda.

| Coluna | Tipo | Descrição |
|---|---|---|
| id_canal | Número inteiro | Código único do canal |
| nome_canal | Texto | Nome do canal de venda |

Canais utilizados:

- E-commerce
- Farmácias
- Perfumarias
- Supermercados
- Marketplace

---

## Tabela: dim_regioes

Armazena as regiões atendidas pela empresa.

| Coluna | Tipo | Descrição |
|---|---|---|
| id_regiao | Número inteiro | Código único da região |
| nome_regiao | Texto | Nome da região brasileira |

Regiões utilizadas:

- Norte
- Nordeste
- Centro-Oeste
- Sudeste
- Sul

---

## Tabela: dim_calendario

Armazena as informações de data.

| Coluna | Tipo | Descrição |
|---|---|---|
| data | Data | Data completa |
| dia | Número inteiro | Dia do mês |
| mes_numero | Número inteiro | Número do mês |
| mes_nome | Texto | Nome do mês |
| trimestre | Texto | Trimestre do ano |
| ano | Número inteiro | Ano |
| ano_mes | Texto | Combinação de ano e mês |

---

## Tabela: fato_vendas

Armazena as vendas realizadas.

| Coluna | Tipo | Descrição |
|---|---|---|
| id_venda | Número inteiro | Código único da linha de venda |
| id_pedido | Número inteiro | Número do pedido |
| data_venda | Data | Data da venda |
| id_produto | Número inteiro | Produto vendido |
| id_canal | Número inteiro | Canal em que a venda aconteceu |
| id_regiao | Número inteiro | Região da venda |
| quantidade | Número inteiro | Quantidade vendida |
| preco_unitario | Número decimal | Preço unitário praticado |
| custo_unitario | Número decimal | Custo unitário na data da venda |
| desconto_percentual | Número decimal | Percentual de desconto |
| receita_bruta | Número decimal | Quantidade multiplicada pelo preço |
| valor_desconto | Número decimal | Valor do desconto concedido |
| receita_liquida | Número decimal | Receita depois do desconto |
| custo_total | Número decimal | Custo total dos produtos |
| margem_bruta | Número decimal | Receita líquida menos custo total |
| margem_percentual | Número decimal | Margem bruta dividida pela receita líquida, como fração: 0,5851 representa 58,51% |

Cada linha representa um produto em um pedido. Um pedido pode conter
várias linhas; contar pedidos exige códigos distintos. A margem percentual
agregada usa margem total dividida pela receita total.

---

## Tabela: fato_orcamento

Armazena os valores planejados fictícios de janeiro de 2024 a dezembro de
2026, por mês, produto, canal e região. O mês é representado pelo primeiro
dia, sem rateio diário. As metas dos meses com realizado foram geradas a
partir das vendas para fins didáticos; não são um planejamento independente.

| Coluna | Tipo | Descrição |
|---|---|---|
| id_orcamento | Número inteiro | Código único do orçamento |
| mes_referencia | Data | Mês ao qual o orçamento pertence |
| id_produto | Número inteiro | Produto orçado |
| id_canal | Número inteiro | Canal orçado |
| id_regiao | Número inteiro | Região orçada |
| quantidade_orcada | Número inteiro | Quantidade prevista |
| receita_orcada | Número decimal | Receita planejada |
| custo_orcado | Número decimal | Custo planejado |
| margem_orcada | Número decimal | Margem planejada |

---

## View: vw_forecast_receita

A previsão atual usa uma view, sem tabela física fato_forecast. São quatro
linhas mensais, de setembro a dezembro de 2026, com totais da empresa.

| Coluna | Tipo | Descrição |
|---|---|---|
| ano_mes_forecast | Texto | Mês previsto, no formato AAAA-MM |
| receita_base_2025 | Número decimal | Receita do mesmo mês de 2025 |
| crescimento_jan_ago_percentual | Número decimal | Crescimento de jan-ago/2026 sobre jan-ago/2025, em pontos percentuais: 7,66 representa 7,66% |
| receita_forecast | Número decimal | Receita base multiplicada pelo fator de crescimento sem arredondamento intermediário; resultado mensal em centavos |
| status_forecast | Texto | Indica previsão ou base insuficiente |
| receita_orcada | Número decimal | Orçamento do mês previsto |
| variacao_forecast_orcamento | Número decimal | Previsão menos orçamento |
| variacao_forecast_orcamento_percentual | Número decimal | Diferença dividida pelo orçamento e multiplicada por 100 |
| status_comparacao | Texto | Situação da previsão frente ao orçamento ou ausência de base |

O Power Query acrescenta mes_referencia, do tipo data, com o primeiro dia
do mês para relacionar o forecast ao calendário. Essa coluna não existe
na view SQL. Não há detalhamento por produto, canal ou região, nem previsão
de custos e margem. A view consulta os dados atuais e não guarda versões
históricas. O orçamento não entra no cálculo da previsão.
