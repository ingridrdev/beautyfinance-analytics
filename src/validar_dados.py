from pathlib import Path

import numpy as np
import pandas as pd


# Localiza as pastas do projeto
pasta_projeto = Path(__file__).resolve().parent.parent
pasta_raw = pasta_projeto / "data" / "raw"
pasta_processed = pasta_projeto / "data" / "processed"


# Carrega as tabelas
df_vendas = pd.read_csv(
    pasta_processed / "fato_vendas.csv",
    parse_dates=["data_venda"],
)

df_orcamento = pd.read_csv(
    pasta_raw / "fato_orcamento.csv",
    parse_dates=["mes_referencia"],
)

df_produtos = pd.read_csv(
    pasta_raw / "dim_produtos.csv"
)

df_canais = pd.read_csv(
    pasta_raw / "dim_canais.csv"
)

df_regioes = pd.read_csv(
    pasta_raw / "dim_regioes.csv"
)


# Colunas que não podem ter valores vazios
colunas_obrigatorias = [
    "id_venda",
    "id_pedido",
    "data_venda",
    "id_produto",
    "id_canal",
    "id_regiao",
    "quantidade",
    "preco_unitario",
    "custo_unitario",
    "receita_bruta",
    "receita_liquida",
    "custo_total",
    "margem_bruta",
]


# Executa as validações
sem_duplicidades = not df_vendas[
    "id_venda"
].duplicated().any()

sem_valores_vazios = not df_vendas[
    colunas_obrigatorias
].isna().any().any()

produtos_validos = df_vendas["id_produto"].isin(
    df_produtos["id_produto"]
).all()

canais_validos = df_vendas["id_canal"].isin(
    df_canais["id_canal"]
).all()

regioes_validas = df_vendas["id_regiao"].isin(
    df_regioes["id_regiao"]
).all()

datas_validas = (
    df_vendas["data_venda"].min()
    >= pd.Timestamp("2024-01-01")
) and (
    df_vendas["data_venda"].max()
    <= pd.Timestamp("2026-08-31")
)

margem_correta = np.allclose(
    df_vendas["margem_bruta"],
    (
        df_vendas["receita_liquida"]
        - df_vendas["custo_total"]
    ),
    atol=0.01,
)


# Monta o relatório de validação
validacoes = pd.DataFrame(
    [
        {
            "validacao": "IDs de venda sem duplicidade",
            "status": "OK" if sem_duplicidades else "ERRO",
        },
        {
            "validacao": "Colunas obrigatórias sem valores vazios",
            "status": "OK" if sem_valores_vazios else "ERRO",
        },
        {
            "validacao": "Produtos existentes na dimensão",
            "status": "OK" if produtos_validos else "ERRO",
        },
        {
            "validacao": "Canais existentes na dimensão",
            "status": "OK" if canais_validos else "ERRO",
        },
        {
            "validacao": "Regiões existentes na dimensão",
            "status": "OK" if regioes_validas else "ERRO",
        },
        {
            "validacao": "Datas dentro do período esperado",
            "status": "OK" if datas_validas else "ERRO",
        },
        {
            "validacao": "Cálculo da margem bruta",
            "status": "OK" if margem_correta else "ERRO",
        },
    ]
)


# Calcula os indicadores gerais
receita_liquida = df_vendas["receita_liquida"].sum()
custo_total = df_vendas["custo_total"].sum()
margem_bruta = df_vendas["margem_bruta"].sum()
quantidade_pedidos = df_vendas["id_pedido"].nunique()
unidades_vendidas = df_vendas["quantidade"].sum()

margem_percentual = (
    margem_bruta / receita_liquida
)

ticket_medio = (
    receita_liquida / quantidade_pedidos
)


# Compara o realizado com o orçamento até o último mês realizado
ultimo_mes_realizado = (
    df_vendas["data_venda"]
    .max()
    .to_period("M")
    .to_timestamp()
)

orcamento_comparavel = df_orcamento[
    df_orcamento["mes_referencia"]
    <= ultimo_mes_realizado
].copy()

receita_orcada = orcamento_comparavel[
    "receita_orcada"
].sum()

variacao_orcamento = (
    receita_liquida - receita_orcada
)

variacao_orcamento_percentual = (
    variacao_orcamento / receita_orcada
)


# Cria o resumo executivo
resumo_executivo = pd.DataFrame(
    [
        {
            "receita_liquida": round(receita_liquida, 2),
            "custo_total": round(custo_total, 2),
            "margem_bruta": round(margem_bruta, 2),
            "margem_percentual": round(
                margem_percentual,
                4,
            ),
            "quantidade_pedidos": quantidade_pedidos,
            "unidades_vendidas": unidades_vendidas,
            "ticket_medio": round(ticket_medio, 2),
            "receita_orcada": round(receita_orcada, 2),
            "variacao_orcamento": round(
                variacao_orcamento,
                2,
            ),
            "variacao_orcamento_percentual": round(
                variacao_orcamento_percentual,
                4,
            ),
        }
    ]
)


# Cria um resumo anual
df_vendas["ano"] = df_vendas["data_venda"].dt.year

resumo_anual = (
    df_vendas.groupby(
        "ano",
        as_index=False,
    )
    .agg(
        receita_liquida=("receita_liquida", "sum"),
        custo_total=("custo_total", "sum"),
        margem_bruta=("margem_bruta", "sum"),
        quantidade_pedidos=("id_pedido", "nunique"),
        unidades_vendidas=("quantidade", "sum"),
    )
)

resumo_anual["margem_percentual"] = (
    resumo_anual["margem_bruta"]
    / resumo_anual["receita_liquida"]
).round(4)

resumo_anual["ticket_medio"] = (
    resumo_anual["receita_liquida"]
    / resumo_anual["quantidade_pedidos"]
).round(2)


# Arredonda as colunas financeiras
colunas_financeiras = [
    "receita_liquida",
    "custo_total",
    "margem_bruta",
]

resumo_anual[colunas_financeiras] = (
    resumo_anual[colunas_financeiras].round(2)
)


# Salva os resultados da validação
validacoes.to_csv(
    pasta_processed / "validacao_dados.csv",
    index=False,
    encoding="utf-8-sig",
)

resumo_executivo.to_csv(
    pasta_processed / "resumo_executivo.csv",
    index=False,
    encoding="utf-8-sig",
)

resumo_anual.to_csv(
    pasta_processed / "resumo_anual.csv",
    index=False,
    encoding="utf-8-sig",
)


# Função para exibir valores em reais
def formatar_reais(valor):
    valor_formatado = f"{valor:,.2f}"

    valor_formatado = (
        valor_formatado
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )

    return f"R$ {valor_formatado}"


# Exibe os principais resultados
print("Validação concluída!")
print(validacoes.to_string(index=False))
print("Receita líquida:", formatar_reais(receita_liquida))
print("Custo total:", formatar_reais(custo_total))
print("Margem bruta:", formatar_reais(margem_bruta))
print(
    "Margem percentual:",
    f"{margem_percentual:.2%}",
)
print("Quantidade de pedidos:", quantidade_pedidos)
print("Ticket médio:", formatar_reais(ticket_medio))
print("Receita orçada:", formatar_reais(receita_orcada))
print(
    "Variação do orçamento:",
    formatar_reais(variacao_orcamento),
)