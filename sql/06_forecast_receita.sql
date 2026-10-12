-- =====================================================
-- BeautyFinance Analytics: forecast de receita líquida
-- Data de corte da simulação: agosto de 2026.
-- Previsão: setembro a dezembro de 2026.
-- =====================================================
-- Método:
-- 1. Divide a receita de janeiro a agosto de 2026 pela
--    receita de janeiro a agosto de 2025 para obter o fator.
-- 2. Multiplica a receita de cada mês de setembro a dezembro
--    de 2025 por esse fator, sem arredondá-lo antes do cálculo.
-- O crescimento é calculado pelos totais, não pela média das taxas.
-- A previsão mantém o padrão de fim de ano de 2025 e pressupõe
-- continuidade do crescimento recente. Não é uma garantia.
-- Orçamento não é usado como previsão e não é alterado.
-- Ao final, compara a previsão com o orçamento dos mesmos meses.
-- Esta consulta não cria tabelas ou views nem grava dados.

WITH receita_mensal AS (
    SELECT
        ano,
        mes_numero,
        ano_mes,
        SUM(receita_liquida) AS receita_liquida
    FROM public.vw_vendas_detalhadas
    WHERE ano IN (2025, 2026)
    GROUP BY ano, mes_numero, ano_mes
),

receita_comparavel AS (
    SELECT
        SUM(CASE WHEN ano = 2025 THEN receita_liquida END)
            AS receita_jan_ago_2025,
        SUM(CASE WHEN ano = 2026 THEN receita_liquida END)
            AS receita_jan_ago_2026,
        COUNT(CASE WHEN ano = 2025 THEN 1 END) AS meses_2025,
        COUNT(CASE WHEN ano = 2026 THEN 1 END) AS meses_2026
    FROM receita_mensal
    WHERE mes_numero BETWEEN 1 AND 8
),

fator_crescimento AS (
    SELECT
        -- Se faltar um mês ou a base for zero, não gera uma taxa.
        CASE
            WHEN meses_2025 = 8 AND meses_2026 = 8 THEN
                receita_jan_ago_2026 / NULLIF(receita_jan_ago_2025, 0)
        END AS fator
    FROM receita_comparavel
),

forecast AS (
SELECT
    '2026-' || SUBSTR(base.ano_mes, 6, 2) AS ano_mes_forecast,
    ROUND(base.receita_liquida, 2) AS receita_base_2025,
    ROUND((crescimento.fator - 1) * 100, 2)
        AS crescimento_jan_ago_percentual,
    ROUND(base.receita_liquida * crescimento.fator, 2)
        AS receita_forecast,
    CASE
        WHEN crescimento.fator IS NULL THEN 'Base insuficiente'
        ELSE 'Previsão'
    END AS status_forecast
FROM receita_mensal AS base
CROSS JOIN fator_crescimento AS crescimento
WHERE base.ano = 2025
    AND base.mes_numero BETWEEN 9 AND 12
),

orcamento_mensal AS (
    SELECT
        ano_mes,
        SUM(receita_orcada) AS receita_orcada
    FROM public.vw_orcamento_detalhado
    WHERE ano = 2026
        AND mes_numero BETWEEN 9 AND 12
    GROUP BY ano_mes
)

SELECT
    forecast.*,
    ROUND(orcamento.receita_orcada, 2) AS receita_orcada,
    ROUND(forecast.receita_forecast - orcamento.receita_orcada, 2)
        AS variacao_forecast_orcamento,
    ROUND(
        (forecast.receita_forecast - orcamento.receita_orcada)
        / NULLIF(orcamento.receita_orcada, 0) * 100,
        2
    ) AS variacao_forecast_orcamento_percentual,
    CASE
        WHEN forecast.receita_forecast IS NULL THEN 'Base insuficiente'
        WHEN orcamento.receita_orcada IS NULL THEN 'Sem orçamento'
        WHEN forecast.receita_forecast > orcamento.receita_orcada
            THEN 'Previsão acima do orçamento'
        WHEN forecast.receita_forecast < orcamento.receita_orcada
            THEN 'Previsão abaixo do orçamento'
        ELSE 'Previsão igual ao orçamento'
    END AS status_comparacao
FROM forecast
LEFT JOIN orcamento_mensal AS orcamento
    ON orcamento.ano_mes = forecast.ano_mes_forecast
ORDER BY forecast.ano_mes_forecast;
