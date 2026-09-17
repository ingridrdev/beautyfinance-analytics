from pathlib import Path

import numpy as np
import pandas as pd


# Mantém os resultados iguais em todas as execuções
gerador = np.random.default_rng(42)


# Localiza as pastas do projeto
pasta_projeto = Path(__file__).resolve().parent.parent
pasta_raw = pasta_projeto / "data" / "raw"
pasta_processed = pasta_projeto / "data" / "processed"


# Carrega a base tratada de vendas
df_vendas = pd.read_csv(
    pasta_processed / "fato_vendas.csv",
    parse_dates=["data_venda"],
)


# Cria o mês de referência de cada venda
df_vendas["mes_referencia"] = (
    df_vendas["data_venda"]
    .dt.to_period("M")
    .dt.to_timestamp()
)


# Consolida os resultados por mês, produto, canal e região
vendas_mensais = (
    df_vendas.groupby(
        [
            "mes_referencia",
            "id_produto",
            "id_canal",
            "id_regiao",
        ],
        as_index=False,
    )
    .agg(
        quantidade_realizada=("quantidade", "sum"),
        receita_realizada=("receita_liquida", "sum"),
        custo_realizado=("custo_total", "sum"),
    )
)


# Define diferenças planejadas entre as regiões
fatores_regiao = {
    1: 0.92,
    2: 0.95,
    3: 1.00,
    4: 1.06,
    5: 1.02,
}


# Define diferenças planejadas entre os canais
fatores_canal = {
    1: 1.10,
    2: 1.02,
    3: 0.97,
    4: 0.94,
    5: 1.05,
}


fator_regiao = vendas_mensais["id_regiao"].map(
    fatores_regiao
)

fator_canal = vendas_mensais["id_canal"].map(
    fatores_canal
)

ruido_orcamento = gerador.uniform(
    0.96,
    1.04,
    size=len(vendas_mensais),
)

fator_desempenho = (
    fator_regiao
    * fator_canal
    * ruido_orcamento
)


# Cria o orçamento dos meses que possuem realizado
orcamento_realizado = vendas_mensais[
    [
        "mes_referencia",
        "id_produto",
        "id_canal",
        "id_regiao",
    ]
].copy()


orcamento_realizado["quantidade_orcada"] = np.maximum(
    np.rint(
        vendas_mensais["quantidade_realizada"]
        / fator_desempenho
    ),
    1,
).astype(int)


orcamento_realizado["receita_orcada"] = (
    vendas_mensais["receita_realizada"]
    / fator_desempenho
).round(2)


# Calcula a proporção de custo em relação à receita
proporcao_custo = (
    vendas_mensais["custo_realizado"]
    / vendas_mensais["receita_realizada"]
).clip(0.15, 0.85)


meta_custo = (
    proporcao_custo
    * gerador.uniform(
        0.97,
        1.01,
        size=len(vendas_mensais),
    )
).clip(0.15, 0.85)


orcamento_realizado["custo_orcado"] = (
    orcamento_realizado["receita_orcada"]
    * meta_custo
).round(2)


orcamento_realizado["margem_orcada"] = (
    orcamento_realizado["receita_orcada"]
    - orcamento_realizado["custo_orcado"]
).round(2)


# Seleciona setembro a dezembro de 2025 como base
base_futuro = vendas_mensais[
    (vendas_mensais["mes_referencia"].dt.year == 2025)
    & (vendas_mensais["mes_referencia"].dt.month >= 9)
].copy()


# Cria o orçamento de setembro a dezembro de 2026
orcamento_futuro = base_futuro[
    [
        "mes_referencia",
        "id_produto",
        "id_canal",
        "id_regiao",
    ]
].copy()


orcamento_futuro["mes_referencia"] = (
    orcamento_futuro["mes_referencia"]
    + pd.DateOffset(years=1)
)


orcamento_futuro["quantidade_orcada"] = np.maximum(
    np.rint(
        base_futuro["quantidade_realizada"] * 1.12
    ),
    1,
).astype(int)


orcamento_futuro["receita_orcada"] = (
    base_futuro["receita_realizada"] * 1.15
).round(2)


orcamento_futuro["custo_orcado"] = (
    base_futuro["custo_realizado"] * 1.10
).round(2)


orcamento_futuro["margem_orcada"] = (
    orcamento_futuro["receita_orcada"]
    - orcamento_futuro["custo_orcado"]
).round(2)


# Junta todo o orçamento
df_orcamento = pd.concat(
    [
        orcamento_realizado,
        orcamento_futuro,
    ],
    ignore_index=True,
)


# Organiza a tabela
df_orcamento = df_orcamento.sort_values(
    by=[
        "mes_referencia",
        "id_produto",
        "id_canal",
        "id_regiao",
    ]
).reset_index(drop=True)


# Cria um identificador único
df_orcamento.insert(
    0,
    "id_orcamento",
    range(1, len(df_orcamento) + 1),
)


# Salva a tabela de orçamento
df_orcamento.to_csv(
    pasta_raw / "fato_orcamento.csv",
    index=False,
    encoding="utf-8-sig",
    date_format="%Y-%m-%d",
)


print("Tabela de orçamento criada com sucesso!")
print(f"Quantidade de registros: {len(df_orcamento)}")
print(
    "Primeiro mês:",
    df_orcamento["mes_referencia"].min(),
)
print(
    "Último mês:",
    df_orcamento["mes_referencia"].max(),
)