-- =====================================================
-- BeautyFinance Analytics
-- Validação da carga de dados no PostgreSQL
-- =====================================================

WITH resumo_vendas AS (
    SELECT
        ROUND(SUM(receita_liquida), 2) AS receita_liquida,
        ROUND(SUM(custo_total), 2) AS custo_total,
        ROUND(SUM(margem_bruta), 2) AS margem_bruta,
        ROUND(
            SUM(margem_bruta) / NULLIF(SUM(receita_liquida), 0) * 100,
            2
        ) AS margem_percentual,
        COUNT(DISTINCT id_pedido) AS quantidade_pedidos,
        ROUND(
            SUM(receita_liquida) / NULLIF(COUNT(DISTINCT id_pedido), 0),
            2
        ) AS ticket_medio
    FROM public.fato_vendas
),

resumo_orcamento AS (
    SELECT
        ROUND(SUM(receita_orcada), 2) AS receita_orcada
    FROM public.fato_orcamento
    WHERE mes_referencia <= DATE '2026-08-01'
)

SELECT
    (SELECT COUNT(*) FROM public.dim_produtos) AS produtos,
    (SELECT COUNT(*) FROM public.dim_canais) AS canais,
    (SELECT COUNT(*) FROM public.dim_regioes) AS regioes,
    (SELECT COUNT(*) FROM public.dim_calendario) AS datas,
    (SELECT COUNT(*) FROM public.fato_vendas) AS linhas_vendas,
    (SELECT COUNT(*) FROM public.fato_orcamento) AS linhas_orcamento,
    vendas.receita_liquida,
    vendas.custo_total,
    vendas.margem_bruta,
    vendas.margem_percentual,
    vendas.quantidade_pedidos,
    vendas.ticket_medio,
    orcamento.receita_orcada,
    ROUND(
        vendas.receita_liquida - orcamento.receita_orcada,
        2
    ) AS variacao_orcamento,
    ROUND(
        (
            vendas.receita_liquida - orcamento.receita_orcada
        ) / NULLIF(orcamento.receita_orcada, 0) * 100,
        2
    ) AS variacao_percentual
FROM resumo_vendas AS vendas
CROSS JOIN resumo_orcamento AS orcamento;