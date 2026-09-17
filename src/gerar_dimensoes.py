from pathlib import Path

import pandas as pd


# Localiza a pasta principal do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Define onde os arquivos serão salvos
pasta_raw = pasta_projeto / "data" / "raw"

# Cria a pasta caso ela ainda não exista
pasta_raw.mkdir(parents=True, exist_ok=True)


# Lista de canais de venda
canais = [
    {"id_canal": 1, "nome_canal": "E-commerce"},
    {"id_canal": 2, "nome_canal": "Farmácias"},
    {"id_canal": 3, "nome_canal": "Perfumarias"},
    {"id_canal": 4, "nome_canal": "Supermercados"},
    {"id_canal": 5, "nome_canal": "Marketplace"},
]


# Lista de regiões
regioes = [
    {"id_regiao": 1, "nome_regiao": "Norte"},
    {"id_regiao": 2, "nome_regiao": "Nordeste"},
    {"id_regiao": 3, "nome_regiao": "Centro-Oeste"},
    {"id_regiao": 4, "nome_regiao": "Sudeste"},
    {"id_regiao": 5, "nome_regiao": "Sul"},
]


# Transforma as listas em tabelas do Pandas
df_canais = pd.DataFrame(canais)
df_regioes = pd.DataFrame(regioes)


# Salva as tabelas em arquivos CSV
df_canais.to_csv(
    pasta_raw / "dim_canais.csv",
    index=False,
    encoding="utf-8-sig",
)

df_regioes.to_csv(
    pasta_raw / "dim_regioes.csv",
    index=False,
    encoding="utf-8-sig",
)


print("Tabelas criadas com sucesso!")
print(f"Canais: {len(df_canais)} registros")
print(f"Regiões: {len(df_regioes)} registros")