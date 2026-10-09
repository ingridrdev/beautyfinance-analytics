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
    -- =====================================================
-- Desempenho financeiro por marca e categoria
-- =====================================================

SELECT
    marca,
    categoria,

    ROUND(SUM(receita_liquida), 2)
        AS receita_liquida,

    ROUND(SUM(custo_total), 2)
        AS custo_total,

    ROUND(SUM(margem_bruta), 2)
        AS margem_bruta,

    ROUND(
        SUM(margem_bruta)
        / NULLIF(SUM(receita_liquida), 0) * 100,
        2
    ) AS margem_percentual,

    SUM(quantidade)
        AS quantidade_vendida,

    COUNT(DISTINCT id_pedido)
        AS quantidade_pedidos,

    ROUND(
        SUM(receita_liquida)
        / NULLIF(COUNT(DISTINCT id_pedido), 0),
        2
    ) AS ticket_medio

FROM public.vw_vendas_detalhadas

GROUP BY
    marca,
    categoria

ORDER BY
    receita_liquida DESC;
    -- =====================================================
-- Budget versus Actual por marca e categoria
-- =====================================================

SELECT
    marca,
    categoria,

    ROUND(SUM(receita_realizada), 2)
        AS receita_realizada,

    ROUND(SUM(receita_orcada), 2)
        AS receita_orcada,

    ROUND(
        SUM(receita_realizada) - SUM(receita_orcada),
        2
    ) AS variacao_receita,

    ROUND(
        (
            SUM(receita_realizada) - SUM(receita_orcada)
        )
        / NULLIF(SUM(receita_orcada), 0) * 100,
        2
    ) AS variacao_percentual,

    ROUND(
        SUM(margem_realizada)
        / NULLIF(SUM(receita_realizada), 0) * 100,
        2
    ) AS margem_percentual_realizada,

    ROUND(
        SUM(margem_orcada)
        / NULLIF(SUM(receita_orcada), 0) * 100,
        2
    ) AS margem_percentual_orcada,

    CASE
        WHEN SUM(receita_realizada) > SUM(receita_orcada)
            THEN 'Acima do orçamento'
        WHEN SUM(receita_realizada) < SUM(receita_orcada)
            THEN 'Abaixo do orçamento'
        ELSE 'Dentro do orçamento'
    END AS status_orcamento

FROM public.vw_budget_actual

WHERE mes_referencia <= DATE '2026-08-01'

GROUP BY
    marca,
    categoria

ORDER BY
    variacao_percentual ASC;
    -- =====================================================
-- Desempenho financeiro por produto
-- =====================================================

SELECT
    nome_produto,
    marca,
    categoria,

    ROUND(SUM(receita_liquida), 2)
        AS receita_liquida,

    ROUND(SUM(custo_total), 2)
        AS custo_total,

    ROUND(SUM(margem_bruta), 2)
        AS margem_bruta,

    ROUND(
        SUM(margem_bruta)
        / NULLIF(SUM(receita_liquida), 0) * 100,
        2
    ) AS margem_percentual,

    SUM(quantidade)
        AS quantidade_vendida,

    COUNT(DISTINCT id_pedido)
        AS quantidade_pedidos,

    ROUND(
        SUM(receita_liquida)
        / NULLIF(COUNT(DISTINCT id_pedido), 0),
        2
    ) AS ticket_medio

FROM public.vw_vendas_detalhadas

GROUP BY
    nome_produto,
    marca,
    categoria

ORDER BY
    receita_liquida DESC;
    -- =====================================================
-- Desempenho financeiro por canal de venda
-- =====================================================

SELECT
    nome_canal,

    ROUND(SUM(receita_liquida), 2)
        AS receita_liquida,

    ROUND(SUM(custo_total), 2)
        AS custo_total,

    ROUND(SUM(margem_bruta), 2)
        AS margem_bruta,

    ROUND(
        SUM(margem_bruta)
        / NULLIF(SUM(receita_liquida), 0) * 100,
        2
    ) AS margem_percentual,

    SUM(quantidade)
        AS quantidade_vendida,

    COUNT(DISTINCT id_pedido)
        AS quantidade_pedidos,

    ROUND(
        SUM(receita_liquida)
        / NULLIF(COUNT(DISTINCT id_pedido), 0),
        2
    ) AS ticket_medio,

    ROUND(
        SUM(receita_liquida)
        / SUM(SUM(receita_liquida)) OVER () * 100,
        2
    ) AS participacao_na_receita

FROM public.vw_vendas_detalhadas

GROUP BY
    nome_canal

ORDER BY
    receita_liquida DESC;
    -- =====================================================
-- Desempenho financeiro por região
-- =====================================================

SELECT
    nome_regiao,

    ROUND(SUM(receita_liquida), 2)
        AS receita_liquida,

    ROUND(SUM(custo_total), 2)
        AS custo_total,

    ROUND(SUM(margem_bruta), 2)
        AS margem_bruta,

    ROUND(
        SUM(margem_bruta)
        / NULLIF(SUM(receita_liquida), 0) * 100,
        2
    ) AS margem_percentual,

    SUM(quantidade)
        AS quantidade_vendida,

    COUNT(DISTINCT id_pedido)
        AS quantidade_pedidos,

    ROUND(
        SUM(receita_liquida)
        / NULLIF(COUNT(DISTINCT id_pedido), 0),
        2
    ) AS ticket_medio,

    ROUND(
        SUM(receita_liquida)
        / SUM(SUM(receita_liquida)) OVER () * 100,
        2
    ) AS participacao_na_receita

FROM public.vw_vendas_detalhadas

GROUP BY
    nome_regiao

ORDER BY
    receita_liquida DESC;


-- =====================================================
-- Crescimento mensal da receita líquida (MoM)
-- Compara cada mês com o mês anterior, inclusive entre anos.
-- Usa somente vendas realizadas; meses futuros não entram.
-- =====================================================

WITH receita_mensal AS (
    SELECT
        ano,
        mes_numero,
        ano_mes,
        SUM(receita_liquida) AS receita_liquida
    FROM public.vw_vendas_detalhadas
    GROUP BY
        ano,
        mes_numero,
        ano_mes
),

comparacao_mensal AS (
    SELECT
        ano,
        mes_numero,
        ano_mes,
        receita_liquida,
        LAG(receita_liquida) OVER (
            ORDER BY ano, mes_numero
        ) AS receita_mes_anterior
    FROM receita_mensal
)

SELECT
    ano_mes,
    ROUND(receita_liquida, 2) AS receita_liquida,
    ROUND(receita_mes_anterior, 2) AS receita_mes_anterior,
    ROUND(
        receita_liquida - receita_mes_anterior,
        2
    ) AS variacao_receita,
    -- NULL indica ausência de comparação ou base igual a zero.
    ROUND(
        (receita_liquida - receita_mes_anterior)
        / NULLIF(receita_mes_anterior, 0) * 100,
        2
    ) AS crescimento_mensal_percentual
FROM comparacao_mensal
ORDER BY
    ano,
    mes_numero;

-- =====================================================
-- Crescimento anual da receita líquida (YoY)
-- Compara cada mês com o mesmo mês do ano anterior.
-- Usa somente vendas realizadas; meses futuros não entram.
-- =====================================================

WITH receita_mensal_anual AS (
    SELECT
        ano,
        mes_numero,
        ano_mes,
        SUM(receita_liquida) AS receita_liquida
    FROM public.vw_vendas_detalhadas
    GROUP BY
        ano,
        mes_numero,
        ano_mes
)

SELECT
    atual.ano_mes,
    ROUND(atual.receita_liquida, 2) AS receita_liquida,
    ROUND(anterior.receita_liquida, 2) AS receita_mes_ano_anterior,
    ROUND(
        atual.receita_liquida - anterior.receita_liquida,
        2
    ) AS variacao_receita_anual,
    -- NULL indica ausência de comparação ou base igual a zero.
    ROUND(
        (atual.receita_liquida - anterior.receita_liquida)
        / NULLIF(anterior.receita_liquida, 0) * 100,
        2
    ) AS crescimento_anual_percentual
FROM receita_mensal_anual AS atual
LEFT JOIN receita_mensal_anual AS anterior
    ON anterior.ano = atual.ano - 1
    AND anterior.mes_numero = atual.mes_numero
ORDER BY
    atual.ano,
    atual.mes_numero;
