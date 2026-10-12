-- =====================================================
-- View do forecast de receita líquida para o Power BI
-- Depende de vw_vendas_detalhadas e vw_orcamento_detalhado.
-- Mesma regra e mesmas colunas da consulta do arquivo 06.
-- Corte fixo: agosto de 2026; previsão: setembro a dezembro.
-- Uma linha por mês, com valores totais da empresa.
-- Não há detalhamento por produto, canal ou região.
-- A view consulta os dados atuais; não guarda uma cópia fixa.
-- security_invoker mantém a verificação de acesso do usuário.
-- Este arquivo cria a view, sem alterar as tabelas de origem.
-- =====================================================

CREATE OR REPLACE VIEW public.vw_forecast_receita
WITH (security_invoker = true)
AS
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
