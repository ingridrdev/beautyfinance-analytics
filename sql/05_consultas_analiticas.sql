-- =====================================================
-- BeautyFinance Analytics
-- Análise mensal de realizado versus orçamento
-- =====================================================

SELECT
    ano,
    mes_numero,
    mes_nome,
    ano_mes,

    ROUND(SUM(receita_realizada), 2)
        AS receita_realizada,

    ROUND(SUM(receita_orcada), 2)
        AS receita_orcada,

    CASE
        WHEN SUM(receita_realizada) = 0 THEN NULL
        ELSE ROUND(
            SUM(receita_realizada) - SUM(receita_orcada),
            2
        )
    END AS variacao_receita,

    CASE
        WHEN SUM(receita_realizada) = 0 THEN NULL
        ELSE ROUND(
            (
                SUM(receita_realizada) - SUM(receita_orcada)
            )
            / NULLIF(SUM(receita_orcada), 0) * 100,
            2
        )
    END AS variacao_percentual,

    CASE
        WHEN SUM(receita_realizada) = 0
            THEN 'Sem realizado'
        WHEN SUM(receita_realizada) > SUM(receita_orcada)
            THEN 'Acima do orçamento'
        WHEN SUM(receita_realizada) < SUM(receita_orcada)
            THEN 'Abaixo do orçamento'
        ELSE 'Dentro do orçamento'
    END AS status_mes

FROM public.vw_budget_actual

GROUP BY
    ano,
    mes_numero,
    mes_nome,
    ano_mes

ORDER BY
    ano,
    mes_numero;