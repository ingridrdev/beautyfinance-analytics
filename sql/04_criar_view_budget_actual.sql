-- =====================================================
-- BeautyFinance Analytics
-- View de comparação entre realizado e orçamento
-- =====================================================

CREATE OR REPLACE VIEW public.vw_budget_actual
WITH (security_invoker = true)
AS

WITH realizado AS (
    SELECT
        DATE_TRUNC('month', data_venda)::DATE AS mes_referencia,
        id_produto,
        id_canal,
        id_regiao,
        SUM(quantidade) AS quantidade_realizada,
        SUM(receita_liquida) AS receita_realizada,
        SUM(custo_total) AS custo_realizado,
        SUM(margem_bruta) AS margem_realizada
    FROM public.fato_vendas
    GROUP BY
        DATE_TRUNC('month', data_venda)::DATE,
        id_produto,
        id_canal,
        id_regiao
),

orcamento AS (
    SELECT
        mes_referencia,
        id_produto,
        id_canal,
        id_regiao,
        SUM(quantidade_orcada) AS quantidade_orcada,
        SUM(receita_orcada) AS receita_orcada,
        SUM(custo_orcado) AS custo_orcado,
        SUM(margem_orcada) AS margem_orcada
    FROM public.fato_orcamento
    GROUP BY
        mes_referencia,
        id_produto,
        id_canal,
        id_regiao
)

SELECT
    COALESCE(realizado.mes_referencia, orcamento.mes_referencia)
        AS mes_referencia,

    calendario.mes_numero,
    calendario.mes_nome,
    calendario.trimestre,
    calendario.ano,
    calendario.ano_mes,

    COALESCE(realizado.id_produto, orcamento.id_produto)
        AS id_produto,
    produtos.nome_produto,
    produtos.marca,
    produtos.categoria,

    COALESCE(realizado.id_canal, orcamento.id_canal)
        AS id_canal,
    canais.nome_canal,

    COALESCE(realizado.id_regiao, orcamento.id_regiao)
        AS id_regiao,
    regioes.nome_regiao,

    COALESCE(realizado.quantidade_realizada, 0)
        AS quantidade_realizada,
    COALESCE(orcamento.quantidade_orcada, 0)
        AS quantidade_orcada,

    COALESCE(realizado.receita_realizada, 0)
        AS receita_realizada,
    COALESCE(orcamento.receita_orcada, 0)
        AS receita_orcada,

    COALESCE(realizado.custo_realizado, 0)
        AS custo_realizado,
    COALESCE(orcamento.custo_orcado, 0)
        AS custo_orcado,

    COALESCE(realizado.margem_realizada, 0)
        AS margem_realizada,
    COALESCE(orcamento.margem_orcada, 0)
        AS margem_orcada,

    ROUND(
        realizado.margem_realizada
        / NULLIF(realizado.receita_realizada, 0) * 100,
        2
    ) AS margem_percentual_realizada,

    ROUND(
        orcamento.margem_orcada
        / NULLIF(orcamento.receita_orcada, 0) * 100,
        2
    ) AS margem_percentual_orcada,

    CASE
        WHEN realizado.mes_referencia IS NULL THEN NULL
        ELSE ROUND(
            realizado.receita_realizada - orcamento.receita_orcada,
            2
        )
    END AS variacao_receita,

    CASE
        WHEN realizado.mes_referencia IS NULL THEN NULL
        ELSE ROUND(
            (
                realizado.receita_realizada - orcamento.receita_orcada
            )
            / NULLIF(orcamento.receita_orcada, 0) * 100,
            2
        )
    END AS variacao_receita_percentual,

    CASE
        WHEN realizado.mes_referencia IS NULL
            THEN 'Sem realizado'
        WHEN realizado.receita_realizada > orcamento.receita_orcada
            THEN 'Acima do orçamento'
        WHEN realizado.receita_realizada < orcamento.receita_orcada
            THEN 'Abaixo do orçamento'
        ELSE 'Dentro do orçamento'
    END AS status_orcamento

FROM realizado

FULL OUTER JOIN orcamento
    ON realizado.mes_referencia = orcamento.mes_referencia
    AND realizado.id_produto = orcamento.id_produto
    AND realizado.id_canal = orcamento.id_canal
    AND realizado.id_regiao = orcamento.id_regiao

INNER JOIN public.dim_produtos AS produtos
    ON produtos.id_produto =
        COALESCE(realizado.id_produto, orcamento.id_produto)

INNER JOIN public.dim_canais AS canais
    ON canais.id_canal =
        COALESCE(realizado.id_canal, orcamento.id_canal)

INNER JOIN public.dim_regioes AS regioes
    ON regioes.id_regiao =
        COALESCE(realizado.id_regiao, orcamento.id_regiao)

INNER JOIN public.dim_calendario AS calendario
    ON calendario.data =
        COALESCE(realizado.mes_referencia, orcamento.mes_referencia);