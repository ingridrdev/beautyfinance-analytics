-- =====================================================
-- Validação histórica do forecast de receita (backtest)
-- Simula uma previsão feita no encerramento de agosto de 2025.
-- O fator usa somente janeiro a agosto de 2024 e de 2025.
-- A base da previsão é setembro a dezembro de 2024.
-- As vendas de setembro a dezembro de 2025 servem SOMENTE
-- para conferir o erro, nunca para calcular a previsão.
-- Esta consulta apenas lê dados; não cria nem altera tabelas.
-- =====================================================
-- Erro = previsão - realizado. Positivo indica superestimação.
-- Erro absoluto percentual ignora o sinal do erro.
-- WAPE = soma dos erros absolutos / soma do realizado * 100.
-- WAPE é ponderado pela receita; menor valor indica menor erro.
-- Um único teste de quatro meses não garante acerto em 2026.

WITH receita_mensal AS (
    SELECT
        ano,
        mes_numero,
        SUM(receita_liquida) AS receita_liquida
    FROM public.vw_vendas_detalhadas
    WHERE ano IN (2024, 2025)
    GROUP BY ano, mes_numero
),

receita_comparavel AS (
    SELECT
        SUM(CASE WHEN ano = 2024 THEN receita_liquida END) AS base_2024,
        SUM(CASE WHEN ano = 2025 THEN receita_liquida END) AS base_2025,
        COUNT(CASE WHEN ano = 2024 THEN 1 END) AS meses_2024,
        COUNT(CASE WHEN ano = 2025 THEN 1 END) AS meses_2025
    FROM receita_mensal
    WHERE mes_numero BETWEEN 1 AND 8
),

fator_crescimento AS (
    SELECT
        CASE
            WHEN meses_2024 = 8 AND meses_2025 = 8 THEN
                base_2025 / NULLIF(base_2024, 0)
        END AS fator
    FROM receita_comparavel
),

meses_avaliacao AS (
    SELECT 9 AS mes_numero
    UNION ALL SELECT 10
    UNION ALL SELECT 11
    UNION ALL SELECT 12
),

comparacao AS (
    SELECT
        meses.mes_numero,
        ROUND(base.receita_liquida * crescimento.fator, 2)
            AS receita_prevista,
        realizado.receita_liquida AS receita_realizada
    FROM meses_avaliacao AS meses
    CROSS JOIN fator_crescimento AS crescimento
    LEFT JOIN receita_mensal AS base
        ON base.ano = 2024 AND base.mes_numero = meses.mes_numero
    LEFT JOIN receita_mensal AS realizado
        ON realizado.ano = 2025 AND realizado.mes_numero = meses.mes_numero
),

erros AS (
    SELECT
        mes_numero,
        receita_prevista,
        receita_realizada,
        receita_prevista - receita_realizada AS erro_receita
    FROM comparacao
)

SELECT
    mes_numero,
    receita_prevista,
    ROUND(receita_realizada, 2) AS receita_realizada,
    ROUND(erro_receita, 2) AS erro_receita,
    ROUND(erro_receita / NULLIF(receita_realizada, 0) * 100, 2)
        AS erro_percentual,
    ROUND(ABS(erro_receita) / NULLIF(ABS(receita_realizada), 0) * 100, 2)
        AS erro_absoluto_percentual,
    -- O indicador do período se repete nas quatro linhas.
    -- Só calcula WAPE se os quatro pares estiverem completos.
    CASE WHEN COUNT(erro_receita) OVER () = 4 THEN
        ROUND(
            SUM(ABS(erro_receita)) OVER ()
            / NULLIF(SUM(ABS(receita_realizada)) OVER (), 0) * 100,
            2
        )
    END AS wape_periodo_percentual
FROM erros
ORDER BY mes_numero;
