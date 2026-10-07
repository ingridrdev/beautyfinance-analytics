-- =====================================================
-- BeautyFinance Analytics
-- Criação das tabelas do banco de dados
-- =====================================================


-- Tabela de produtos
CREATE TABLE IF NOT EXISTS public.dim_produtos (
    id_produto INTEGER PRIMARY KEY,
    nome_produto TEXT NOT NULL,
    marca TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco_sugerido NUMERIC(12, 2) NOT NULL,
    custo_base NUMERIC(12, 2) NOT NULL,
    data_lancamento DATE NOT NULL,
    status_produto TEXT NOT NULL
);


-- Tabela de canais de venda
CREATE TABLE IF NOT EXISTS public.dim_canais (
    id_canal INTEGER PRIMARY KEY,
    nome_canal TEXT NOT NULL
);


-- Tabela de regiões
CREATE TABLE IF NOT EXISTS public.dim_regioes (
    id_regiao INTEGER PRIMARY KEY,
    nome_regiao TEXT NOT NULL
);


-- Tabela de calendário
CREATE TABLE IF NOT EXISTS public.dim_calendario (
    data DATE PRIMARY KEY,
    dia INTEGER NOT NULL,
    mes_numero INTEGER NOT NULL,
    mes_nome TEXT NOT NULL,
    trimestre INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    ano_mes TEXT NOT NULL
);


-- Tabela de vendas realizadas
CREATE TABLE IF NOT EXISTS public.fato_vendas (
    id_venda INTEGER PRIMARY KEY,
    id_pedido INTEGER NOT NULL,
    data_venda DATE NOT NULL,
    id_produto INTEGER NOT NULL,
    id_canal INTEGER NOT NULL,
    id_regiao INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario NUMERIC(12, 2) NOT NULL,
    custo_unitario NUMERIC(12, 2) NOT NULL,
    desconto_percentual NUMERIC(10, 4) NOT NULL,
    receita_bruta NUMERIC(14, 2) NOT NULL,
    valor_desconto NUMERIC(14, 2) NOT NULL,
    receita_liquida NUMERIC(14, 2) NOT NULL,
    custo_total NUMERIC(14, 2) NOT NULL,
    margem_bruta NUMERIC(14, 2) NOT NULL,
    margem_percentual NUMERIC(10, 4) NOT NULL,

    CONSTRAINT fk_vendas_calendario
        FOREIGN KEY (data_venda)
        REFERENCES public.dim_calendario (data),

    CONSTRAINT fk_vendas_produto
        FOREIGN KEY (id_produto)
        REFERENCES public.dim_produtos (id_produto),

    CONSTRAINT fk_vendas_canal
        FOREIGN KEY (id_canal)
        REFERENCES public.dim_canais (id_canal),

    CONSTRAINT fk_vendas_regiao
        FOREIGN KEY (id_regiao)
        REFERENCES public.dim_regioes (id_regiao)
);


-- Tabela de orçamento
CREATE TABLE IF NOT EXISTS public.fato_orcamento (
    id_orcamento INTEGER PRIMARY KEY,
    mes_referencia DATE NOT NULL,
    id_produto INTEGER NOT NULL,
    id_canal INTEGER NOT NULL,
    id_regiao INTEGER NOT NULL,
    quantidade_orcada INTEGER NOT NULL,
    receita_orcada NUMERIC(14, 2) NOT NULL,
    custo_orcado NUMERIC(14, 2) NOT NULL,
    margem_orcada NUMERIC(14, 2) NOT NULL,

    CONSTRAINT fk_orcamento_calendario
        FOREIGN KEY (mes_referencia)
        REFERENCES public.dim_calendario (data),

    CONSTRAINT fk_orcamento_produto
        FOREIGN KEY (id_produto)
        REFERENCES public.dim_produtos (id_produto),

    CONSTRAINT fk_orcamento_canal
        FOREIGN KEY (id_canal)
        REFERENCES public.dim_canais (id_canal),

    CONSTRAINT fk_orcamento_regiao
        FOREIGN KEY (id_regiao)
        REFERENCES public.dim_regioes (id_regiao)
);