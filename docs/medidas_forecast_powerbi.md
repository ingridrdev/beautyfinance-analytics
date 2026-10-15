# Medidas de forecast no Power BI

## Medidas criadas

Quatro medidas em vw_forecast_receita, na pasta Forecast:

| Medida | Regra |
|---|---|
| Previsão Receita | Soma da receita prevista da view nos meses selecionados |
| Orçamento Período Forecast | Soma do orçamento da mesma view e dos mesmos meses |
| Variação Forecast Orçamento | Previsão menos orçamento |
| Variação Forecast Orçamento % | Variação dividida pelo orçamento |

O método da previsão não foi alterado. Não se recalcula forecast em DAX;
as medidas usam os resultados já validados da view do Supabase. A taxa
agregada usa os totais, não a média simples dos percentuais das linhas.
DIVIDE protege a divisão por zero. As medidas mantêm valores vazios quando
não existe base no período.

## Escopo dos filtros

O forecast é total da empresa, mensal, de setembro a dezembro de 2026.
Não há distribuição por produto, canal ou região. Quando houver filtro
direto em qualquer uma dessas três dimensões, as quatro medidas ficam
vazias para não apresentar o total como se fosse a previsão do recorte.
ISFILTERED identifica os filtros diretos nas tabelas.
Fonte: [ISFILTERED](https://learn.microsoft.com/en-us/dax/isfiltered-function-dax).

Use os campos das dimensões nos filtros e estas medidas nos visuais.
As colunas brutas da view continuam disponíveis e não aplicam essa proteção.
Não usar IDs das tabelas de fatos para filtrar os visuais de forecast.

Filtrar mês/ano em dim_calendario funciona normalmente. Agosto não tem
previsão; agosto e setembro juntos retornam somente setembro. Um total
sem filtro de mês soma os quatro meses previstos, sem incluir realizado.
O orçamento dessa medida também se limita aos meses previstos. Orçamento
e forecast são mensais, ligados ao primeiro dia do mês; não há rateio diário.

## Testes e execução

A consulta SQL existente foi executada em SQLite na memória com receitas
mensais agregadas dos CSVs. Totais e diferenças foram conferidos com
Decimal. As fórmulas e a cópia da Consulta 1 foram inspecionadas. Nenhuma
origem foi modificada. As proteções de filtro DAX precisam ser confirmadas
no Desktop, pois seu motor não foi executado na validação local.

1. Reabra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Abra Exibição de consulta DAX → Consulta 1.
3. Clique em Executar; o teste já está colocado. Envie as oito linhas.
4. Após a conferência, salve com Ctrl + S. Feche antes de nova edição externa
   e reabra para novos testes, conforme orientação.

O teste também está em powerbi/validar_medidas_forecast.dax. Os testes
anteriores foram preservados. Resultados esperados:

| Cenário | Previsto | Orçamento | Diferença | Variação % |
|---|---:|---:|---:|---:|
| Total forecast | 317.686,24 | 339.334,73 | -21.648,49 | -6,38 |
| Setembro 2026 | 63.645,73 | 67.982,82 | -4.337,09 | -6,38 |
| Dezembro 2026 | 98.709,50 | 105.435,95 | -6.726,45 | -6,38 |
| Agosto 2026 sem forecast | Vazio | Vazio | Vazio | Vazio |
| Agosto e setembro 2026 | 63.645,73 | 67.982,82 | -4.337,09 | -6,38 |
| Canal 1 sem detalhamento | Vazio | Vazio | Vazio | Vazio |
| Produto 1 sem detalhamento | Vazio | Vazio | Vazio | Vazio |
| Região 1 sem detalhamento | Vazio | Vazio | Vazio | Vazio |

A consulta exibe a fração percentual multiplicada por 100 e arredondada
somente para leitura. A medida permanente mantém a fração completa.

## Registro

Nenhuma ação no Supabase. Após conferir e salvar, preparar no Source Control:

- definition/tables/vw_forecast_receita.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_medidas_forecast.dax.
- docs/medidas_forecast_powerbi.md.

Revisar metadados adicionais antes de incluir. Preservar pendências anteriores
de outros arquivos, inclusive docs/relacionamentos_powerbi.md. O progresso
continua no documento local ignorado.
Mensagem: `feat: add forecast revenue measures`.
Fazer Commit e depois ... → Push manualmente após a revisão.
