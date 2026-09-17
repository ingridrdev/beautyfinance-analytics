from pathlib import Path

import pandas as pd


# Localiza a pasta principal do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Define onde o arquivo será salvo
pasta_raw = pasta_projeto / "data" / "raw"
pasta_raw.mkdir(parents=True, exist_ok=True)


# Cria uma sequência com todos os dias do período analisado
datas = pd.date_range(
    start="2024-01-01",
    end="2026-12-31",
    freq="D",
)


# Cria a tabela calendário
df_calendario = pd.DataFrame({"data": datas})


# Dicionário para converter o número do mês em nome
nomes_meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro",
}


# Cria as colunas de data
df_calendario["dia"] = df_calendario["data"].dt.day
df_calendario["mes_numero"] = df_calendario["data"].dt.month
df_calendario["mes_nome"] = df_calendario["mes_numero"].map(nomes_meses)
df_calendario["trimestre"] = (
    "T" + df_calendario["data"].dt.quarter.astype(str)
)
df_calendario["ano"] = df_calendario["data"].dt.year
df_calendario["ano_mes"] = df_calendario["data"].dt.strftime("%Y-%m")


# Salva a tabela em CSV
df_calendario.to_csv(
    pasta_raw / "dim_calendario.csv",
    index=False,
    encoding="utf-8-sig",
)


print("Dimensão calendário criada com sucesso!")
print(f"Quantidade de datas: {len(df_calendario)}")
print(f"Data inicial: {df_calendario['data'].min()}")
print(f"Data final: {df_calendario['data'].max()}")