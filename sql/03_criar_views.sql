-- =====================================================
-- BeautyFinance Analytics
-- Views detalhadas para análises e Power BI
-- =====================================================


-- View com vendas, produtos, canais, regiões e calendário
CREATE OR REPLACE VIEW public.vw_vendas_detalhadas
WITH (security_invoker = true)
AS
SELECT
    vendas.id_venda,
    vendas.id_pedido,
    vendas.data_venda,

    calendario.dia,
    calendario.mes_numero,
    calendario.mes_nome,
    calendario.trimestre,
    calendario.ano,
    calendario.ano_mes,

    vendas.id_produto,
    produtos.nome_produto,
    produtos.marca,
    produtos.categoria,
    produtos.status_produto,

    vendas.id_canal,
    canais.nome_canal,

    vendas.id_regiao,
    regioes.nome_regiao,

    vendas.quantidade,
    vendas.preco_unitario,
    vendas.custo_unitario,
    vendas.desconto_percentual,
    vendas.receita_bruta,
    vendas.valor_desconto,
    vendas.receita_liquida,
    vendas.custo_total,
    vendas.margem_bruta,
    vendas.margem_percentual

FROM public.fato_vendas AS vendas

INNER JOIN public.dim_produtos AS produtos
    ON vendas.id_produto = produtos.id_produto

INNER JOIN public.dim_canais AS canais
    ON vendas.id_canal = canais.id_canal

INNER JOIN public.dim_regioes AS regioes
    ON vendas.id_regiao = regioes.id_regiao

INNER JOIN public.dim_calendario AS calendario
    ON vendas.data_venda = calendario.data;


-- View com orçamento, produtos, canais, regiões e calendário
CREATE OR REPLACE VIEW public.vw_orcamento_detalhado
WITH (security_invoker = true)
AS
SELECT
    orcamento.id_orcamento,
    orcamento.mes_referencia,

    calendario.mes_numero,
    calendario.mes_nome,
    calendario.trimestre,
    calendario.ano,
    calendario.ano_mes,

    orcamento.id_produto,
    produtos.nome_produto,
    produtos.marca,
    produtos.categoria,
    produtos.status_produto,

    orcamento.id_canal,
    canais.nome_canal,

    orcamento.id_regiao,
    regioes.nome_regiao,

    orcamento.quantidade_orcada,
    orcamento.receita_orcada,
    orcamento.custo_orcado,
    orcamento.margem_orcada

FROM public.fato_orcamento AS orcamento

INNER JOIN public.dim_produtos AS produtos
    ON orcamento.id_produto = produtos.id_produto

INNER JOIN public.dim_canais AS canais
    ON orcamento.id_canal = canais.id_canal

INNER JOIN public.dim_regioes AS regioes
    ON orcamento.id_regiao = regioes.id_regiao

INNER JOIN public.dim_calendario AS calendario
    ON orcamento.mes_referencia = calendario.data;