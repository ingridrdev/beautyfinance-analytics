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

Canais previstos:

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

Regiões previstas:

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

---

## Tabela: fato_orcamento

Armazena os valores planejados pela empresa.

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

## Tabela futura: fato_forecast

Esta tabela será criada em uma etapa posterior para guardar as previsões dos próximos meses.