from pathlib import Path

import numpy as np
import pandas as pd


# Localiza as pastas do projeto
pasta_projeto = Path(__file__).resolve().parent.parent
pasta_raw = pasta_projeto / "data" / "raw"
pasta_processed = pasta_projeto / "data" / "processed"

pasta_processed.mkdir(parents=True, exist_ok=True)


# Carrega a base bruta
caminho_entrada = pasta_raw / "fato_vendas_raw.csv"
df_vendas = pd.read_csv(caminho_entrada)


# Guarda informações para o relatório de qualidade
quantidade_inicial = len(df_vendas)

duplicidades_encontradas = df_vendas.duplicated(
    subset=["id_venda"]
).sum()

descontos_vazios_encontrados = df_vendas[
    "desconto_percentual"
].isna().sum()


# Remove registros duplicados
df_vendas = df_vendas.drop_duplicates(
    subset=["id_venda"],
    keep="first",
).copy()


# Preenche descontos vazios com zero
df_vendas["desconto_percentual"] = (
    df_vendas["desconto_percentual"].fillna(0.0)
)


# Converte a coluna de data
df_vendas["data_venda"] = pd.to_datetime(
    df_vendas["data_venda"],
    errors="coerce",
)


# Converte as colunas numéricas
colunas_numericas = [
    "id_venda",
    "id_pedido",
    "id_produto",
    "id_canal",
    "id_regiao",
    "quantidade",
    "preco_unitario",
    "custo_unitario",
    "desconto_percentual",
]

for coluna in colunas_numericas:
    df_vendas[coluna] = pd.to_numeric(
        df_vendas[coluna],
        errors="coerce",
    )


# Remove registros sem informações essenciais
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
    "desconto_percentual",
]

df_vendas = df_vendas.dropna(
    subset=colunas_obrigatorias
).copy()


# Identifica apenas registros com valores válidos
filtro_valido = (
    (df_vendas["quantidade"] > 0)
    & (df_vendas["preco_unitario"] > 0)
    & (df_vendas["custo_unitario"] > 0)
    & (df_vendas["desconto_percentual"] >= 0)
    & (df_vendas["desconto_percentual"] <= 1)
)

quantidade_antes_validacao = len(df_vendas)

df_vendas = df_vendas.loc[filtro_valido].copy()

registros_invalidos_removidos = (
    quantidade_antes_validacao - len(df_vendas)
)


# Ajusta as colunas que devem ser números inteiros
colunas_inteiras = [
    "id_venda",
    "id_pedido",
    "id_produto",
    "id_canal",
    "id_regiao",
    "quantidade",
]

for coluna in colunas_inteiras:
    df_vendas[coluna] = df_vendas[coluna].astype(int)


# Calcula as métricas financeiras
df_vendas["receita_bruta"] = (
    df_vendas["quantidade"]
    * df_vendas["preco_unitario"]
).round(2)

df_vendas["valor_desconto"] = (
    df_vendas["receita_bruta"]
    * df_vendas["desconto_percentual"]
).round(2)

df_vendas["receita_liquida"] = (
    df_vendas["receita_bruta"]
    - df_vendas["valor_desconto"]
).round(2)

df_vendas["custo_total"] = (
    df_vendas["quantidade"]
    * df_vendas["custo_unitario"]
).round(2)

df_vendas["margem_bruta"] = (
    df_vendas["receita_liquida"]
    - df_vendas["custo_total"]
).round(2)

df_vendas["margem_percentual"] = np.where(
    df_vendas["receita_liquida"] > 0,
    df_vendas["margem_bruta"]
    / df_vendas["receita_liquida"],
    0,
).round(4)


# Organiza a tabela por data, pedido e venda
df_vendas = df_vendas.sort_values(
    by=["data_venda", "id_pedido", "id_venda"]
).reset_index(drop=True)


# Valida a qualidade da base tratada
assert not df_vendas["id_venda"].duplicated().any()
assert not df_vendas[colunas_obrigatorias].isna().any().any()


# Cria um relatório de qualidade dos dados
relatorio_qualidade = pd.DataFrame(
    [
        {
            "indicador": "Linhas na base bruta",
            "valor": quantidade_inicial,
        },
        {
            "indicador": "Duplicidades removidas",
            "valor": int(duplicidades_encontradas),
        },
        {
            "indicador": "Descontos vazios preenchidos",
            "valor": int(descontos_vazios_encontrados),
        },
        {
            "indicador": "Registros inválidos removidos",
            "valor": registros_invalidos_removidos,
        },
        {
            "indicador": "Linhas na base tratada",
            "valor": len(df_vendas),
        },
    ]
)


# Salva a base tratada
df_vendas.to_csv(
    pasta_processed / "fato_vendas.csv",
    index=False,
    encoding="utf-8-sig",
    date_format="%Y-%m-%d",
)


# Salva o relatório de qualidade
relatorio_qualidade.to_csv(
    pasta_processed / "relatorio_qualidade.csv",
    index=False,
    encoding="utf-8-sig",
)


print("Tratamento concluído com sucesso!")
print(f"Linhas na base bruta: {quantidade_inicial}")
print(
    "Duplicidades removidas:",
    int(duplicidades_encontradas),
)
print(
    "Descontos vazios preenchidos:",
    int(descontos_vazios_encontrados),
)
print(
    "Linhas na base tratada:",
    len(df_vendas),
)