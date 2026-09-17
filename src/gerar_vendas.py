from pathlib import Path

import numpy as np
import pandas as pd


# Mantém os mesmos resultados sempre que o código for executado
gerador = np.random.default_rng(42)


# Localiza as pastas do projeto
pasta_projeto = Path(__file__).resolve().parent.parent
pasta_raw = pasta_projeto / "data" / "raw"
pasta_raw.mkdir(parents=True, exist_ok=True)


# Carrega os produtos criados anteriormente
caminho_produtos = pasta_raw / "dim_produtos.csv"
df_produtos = pd.read_csv(caminho_produtos)

dados_produtos = df_produtos.set_index("id_produto")
ids_produtos = df_produtos["id_produto"].to_numpy()


# Define o período realizado
datas = pd.date_range(
    start="2024-01-01",
    end="2026-08-31",
    freq="D",
)


# Dá mais peso aos meses com maior volume de vendas
pesos_datas = np.ones(len(datas), dtype=float)

pesos_datas *= np.where(datas.month == 11, 1.45, 1.00)
pesos_datas *= np.where(datas.month == 12, 1.65, 1.00)
pesos_datas *= np.where(datas.month == 5, 1.15, 1.00)
pesos_datas *= np.where(datas.month == 6, 1.10, 1.00)

# Simula crescimento da empresa ao longo dos anos
pesos_datas *= np.where(datas.year == 2025, 1.08, 1.00)
pesos_datas *= np.where(datas.year == 2026, 1.16, 1.00)

# Converte os pesos em probabilidades
pesos_datas = pesos_datas / pesos_datas.sum()


# Probabilidade de venda de cada produto
pesos_produtos = np.array(
    [
        0.08,
        0.07,
        0.07,
        0.07,
        0.08,
        0.05,
        0.08,
        0.08,
        0.06,
        0.05,
        0.07,
        0.07,
        0.06,
        0.08,
        0.08,
    ]
)

pesos_produtos = pesos_produtos / pesos_produtos.sum()


# Canais e suas probabilidades
ids_canais = [1, 2, 3, 4, 5]
pesos_canais = [0.28, 0.25, 0.18, 0.14, 0.15]


# Regiões e suas probabilidades
ids_regioes = [1, 2, 3, 4, 5]
pesos_regioes = [0.07, 0.18, 0.10, 0.45, 0.20]


# Descontos praticados em cada canal
descontos_por_canal = {
    1: [0.00, 0.05, 0.10, 0.15],
    2: [0.00, 0.05, 0.10],
    3: [0.00, 0.05, 0.10],
    4: [0.00, 0.05],
    5: [0.05, 0.10, 0.15, 0.20],
}


# Quantidade de pedidos que serão gerados
quantidade_pedidos = 15000

vendas = []
id_venda = 1


for numero_pedido in range(quantidade_pedidos):
    id_pedido = 100001 + numero_pedido

    data_venda = pd.Timestamp(
        gerador.choice(datas, p=pesos_datas)
    )

    id_canal = int(
        gerador.choice(ids_canais, p=pesos_canais)
    )

    id_regiao = int(
        gerador.choice(ids_regioes, p=pesos_regioes)
    )

    # Cada pedido pode ter de um a quatro produtos
    quantidade_itens = int(
        gerador.choice(
            [1, 2, 3, 4],
            p=[0.62, 0.27, 0.09, 0.02],
        )
    )

    produtos_pedido = gerador.choice(
        ids_produtos,
        size=quantidade_itens,
        replace=False,
        p=pesos_produtos,
    )

    for id_produto in produtos_pedido:
        id_produto = int(id_produto)

        produto = dados_produtos.loc[id_produto]

        quantidade = int(
            gerador.choice(
                [1, 2, 3, 4],
                p=[0.72, 0.20, 0.06, 0.02],
            )
        )

        # Varia levemente o preço em relação ao preço sugerido
        preco_unitario = round(
            produto["preco_sugerido"]
            * gerador.uniform(0.93, 1.04),
            2,
        )

        # Simula aumento de custo ao longo do tempo
        meses_desde_inicio = (
            (data_venda.year - 2024) * 12
            + data_venda.month
            - 1
        )

        crescimento_custo = 1 + (meses_desde_inicio * 0.004)

        custo_unitario = round(
            produto["custo_base"]
            * crescimento_custo
            * gerador.uniform(0.97, 1.03),
            2,
        )

        desconto_percentual = float(
            gerador.choice(descontos_por_canal[id_canal])
        )

        vendas.append(
            {
                "id_venda": id_venda,
                "id_pedido": id_pedido,
                "data_venda": data_venda.strftime("%Y-%m-%d"),
                "id_produto": id_produto,
                "id_canal": id_canal,
                "id_regiao": id_regiao,
                "quantidade": quantidade,
                "preco_unitario": preco_unitario,
                "custo_unitario": custo_unitario,
                "desconto_percentual": desconto_percentual,
            }
        )

        id_venda += 1


# Transforma a lista de vendas em uma tabela
df_vendas = pd.DataFrame(vendas)


# Adiciona descontos vazios para praticarmos tratamento
indices_vazios = gerador.choice(
    df_vendas.index,
    size=60,
    replace=False,
)

df_vendas.loc[
    indices_vazios,
    "desconto_percentual",
] = np.nan


# Adiciona algumas linhas duplicadas de forma controlada
duplicidades = df_vendas.sample(
    n=25,
    random_state=42,
)

df_vendas = pd.concat(
    [df_vendas, duplicidades],
    ignore_index=True,
)


# Embaralha a base para simular um arquivo recebido
df_vendas = df_vendas.sample(
    frac=1,
    random_state=42,
).reset_index(drop=True)


# Salva a base bruta
df_vendas.to_csv(
    pasta_raw / "fato_vendas_raw.csv",
    index=False,
    encoding="utf-8-sig",
)


print("Base bruta de vendas criada com sucesso!")
print(f"Quantidade de linhas: {len(df_vendas)}")
print(f"Quantidade de pedidos: {df_vendas['id_pedido'].nunique()}")
print(
    "Descontos vazios:",
    df_vendas["desconto_percentual"].isna().sum(),
)
print(
    "IDs de venda duplicados:",
    df_vendas["id_venda"].duplicated().sum(),
)