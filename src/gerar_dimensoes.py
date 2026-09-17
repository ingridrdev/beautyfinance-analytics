from pathlib import Path

import pandas as pd


# Localiza a pasta principal do projeto
pasta_projeto = Path(__file__).resolve().parent.parent

# Define onde os arquivos serão salvos
pasta_raw = pasta_projeto / "data" / "raw"

# Cria a pasta caso ela ainda não exista
pasta_raw.mkdir(parents=True, exist_ok=True)


# Canais de venda
canais = [
    {"id_canal": 1, "nome_canal": "E-commerce"},
    {"id_canal": 2, "nome_canal": "Farmácias"},
    {"id_canal": 3, "nome_canal": "Perfumarias"},
    {"id_canal": 4, "nome_canal": "Supermercados"},
    {"id_canal": 5, "nome_canal": "Marketplace"},
]


# Regiões brasileiras
regioes = [
    {"id_regiao": 1, "nome_regiao": "Norte"},
    {"id_regiao": 2, "nome_regiao": "Nordeste"},
    {"id_regiao": 3, "nome_regiao": "Centro-Oeste"},
    {"id_regiao": 4, "nome_regiao": "Sudeste"},
    {"id_regiao": 5, "nome_regiao": "Sul"},
]


# Produtos fictícios
produtos = [
    {
        "id_produto": 1,
        "nome_produto": "Gel de Limpeza Facial",
        "marca": "Lumera",
        "categoria": "Cuidados com a Pele",
        "preco_sugerido": 69.90,
        "custo_base": 24.50,
        "data_lancamento": "2023-02-15",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 2,
        "nome_produto": "Sérum de Vitamina C",
        "marca": "Lumera",
        "categoria": "Cuidados com a Pele",
        "preco_sugerido": 119.90,
        "custo_base": 42.00,
        "data_lancamento": "2023-05-10",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 3,
        "nome_produto": "Água Micelar",
        "marca": "Lumera",
        "categoria": "Cuidados com a Pele",
        "preco_sugerido": 54.90,
        "custo_base": 18.50,
        "data_lancamento": "2023-08-20",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 4,
        "nome_produto": "Hidratante Facial",
        "marca": "VittaDerm",
        "categoria": "Cuidados com a Pele",
        "preco_sugerido": 89.90,
        "custo_base": 31.00,
        "data_lancamento": "2023-03-12",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 5,
        "nome_produto": "Protetor Solar FPS 60",
        "marca": "VittaDerm",
        "categoria": "Proteção Solar",
        "preco_sugerido": 99.90,
        "custo_base": 38.00,
        "data_lancamento": "2023-09-05",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 6,
        "nome_produto": "Protetor Solar Corporal",
        "marca": "VittaDerm",
        "categoria": "Proteção Solar",
        "preco_sugerido": 79.90,
        "custo_base": 30.00,
        "data_lancamento": "2024-01-15",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 7,
        "nome_produto": "Shampoo Reparador",
        "marca": "Capillare",
        "categoria": "Cuidados com o Cabelo",
        "preco_sugerido": 49.90,
        "custo_base": 17.00,
        "data_lancamento": "2023-04-08",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 8,
        "nome_produto": "Condicionador Nutritivo",
        "marca": "Capillare",
        "categoria": "Cuidados com o Cabelo",
        "preco_sugerido": 52.90,
        "custo_base": 18.50,
        "data_lancamento": "2023-04-08",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 9,
        "nome_produto": "Máscara Capilar",
        "marca": "Capillare",
        "categoria": "Cuidados com o Cabelo",
        "preco_sugerido": 74.90,
        "custo_base": 27.00,
        "data_lancamento": "2023-06-18",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 10,
        "nome_produto": "Óleo Capilar",
        "marca": "Capillare",
        "categoria": "Cuidados com o Cabelo",
        "preco_sugerido": 64.90,
        "custo_base": 22.00,
        "data_lancamento": "2024-02-10",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 11,
        "nome_produto": "Batom Matte",
        "marca": "BellaVie",
        "categoria": "Maquiagem",
        "preco_sugerido": 44.90,
        "custo_base": 12.50,
        "data_lancamento": "2023-07-25",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 12,
        "nome_produto": "Base Líquida",
        "marca": "BellaVie",
        "categoria": "Maquiagem",
        "preco_sugerido": 84.90,
        "custo_base": 26.50,
        "data_lancamento": "2023-10-01",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 13,
        "nome_produto": "Máscara de Cílios",
        "marca": "BellaVie",
        "categoria": "Maquiagem",
        "preco_sugerido": 59.90,
        "custo_base": 19.00,
        "data_lancamento": "2024-03-15",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 14,
        "nome_produto": "Sabonete Corporal",
        "marca": "Essenza",
        "categoria": "Higiene Pessoal",
        "preco_sugerido": 29.90,
        "custo_base": 9.50,
        "data_lancamento": "2023-01-20",
        "status_produto": "Ativo",
    },
    {
        "id_produto": 15,
        "nome_produto": "Hidratante Corporal",
        "marca": "Essenza",
        "categoria": "Higiene Pessoal",
        "preco_sugerido": 59.90,
        "custo_base": 21.00,
        "data_lancamento": "2023-01-20",
        "status_produto": "Ativo",
    },
]


# Transforma as listas em tabelas do Pandas
df_canais = pd.DataFrame(canais)
df_regioes = pd.DataFrame(regioes)
df_produtos = pd.DataFrame(produtos)


# Converte a coluna para o formato de data
df_produtos["data_lancamento"] = pd.to_datetime(
    df_produtos["data_lancamento"]
)


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

df_produtos.to_csv(
    pasta_raw / "dim_produtos.csv",
    index=False,
    encoding="utf-8-sig",
)


print("Tabelas criadas com sucesso!")
print(f"Canais: {len(df_canais)} registros")
print(f"Regiões: {len(df_regioes)} registros")
print(f"Produtos: {len(df_produtos)} registros")