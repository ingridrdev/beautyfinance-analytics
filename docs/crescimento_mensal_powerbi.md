# Crescimento mensal da receita (MoM)

## Medidas

Três medidas em fato_vendas, na pasta Crescimento mensal:

- Receita Mês Anterior: receita deslocada um mês pelo calendário.
- Variação Receita MoM: receita atual menos receita anterior.
- Crescimento Receita MoM %: variação dividida pela receita anterior.

As medidas exigem um único mês completo de dim_calendario e receita
realizada no mês atual. Janeiro de 2024 fica sem comparação por ausência
de 2023. Setembro de 2026 fica sem comparação por ausência de realizado.
Se a receita anterior for zero, DIVIDE retorna vazio para o percentual.

Use ano_mes de dim_calendario nos gráficos e filtros. Totais com vários
meses e filtros por parte de um mês retornam vazio nas três medidas MoM.
Não se somam nem se calculam médias simples das taxas mensais. Os filtros
de produto, canal e região permanecem válidos para o mês anterior.

DATEADD usa a coluna data do calendário marcado como tabela de datas.
Fonte: [DATEADD](https://learn.microsoft.com/en-us/dax/dateadd-function-dax).

## Conferência local

Foram recalculadas receitas mensais com Decimal, conferidos os 32 meses
consecutivos e verificados exemplos do primeiro mês, passagem de ano,
queda, crescimento e filtro de canal. Agosto/2026 coincide com a análise
SQL: diferença 2.744,28 e crescimento 4,83%.
O teste independente é idêntico à Consulta 1 salva. As medidas anteriores
foram preservadas. O motor DAX ainda precisa ser conferido no Desktop.

## Reabrir e testar

1. Abra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Abra Exibição de consulta DAX → Consulta 1.
3. Clique em Executar: o teste já está colocado.
4. Envie as nove linhas retornadas antes de registrar a validação.
5. Após a conferência, salve com Ctrl + S. Feche antes de outra edição
   externa do modelo e reabra para testar, conforme orientação.

Resultados esperados:

| Cenário | Atual | Anterior | Variação | Crescimento % |
|---|---:|---:|---:|---:|
| Janeiro 2024 | 56.985,04 | Vazio | Vazio | Vazio |
| Fevereiro 2024 | 49.487,52 | 56.985,04 | -7.497,52 | -13,16 |
| Novembro 2024 | 80.246,14 | 55.183,27 | 25.062,87 | 45,42 |
| Janeiro 2025 | 52.378,90 | 94.808,11 | -42.429,21 | -44,75 |
| Agosto 2026 | 59.569,39 | 56.825,11 | 2.744,28 | 4,83 |
| Canal 1 agosto 2026 | 15.262,98 | 13.829,93 | 1.433,05 | 10,36 |
| Setembro 2026 sem realizado | Vazio | Vazio | Vazio | Vazio |
| Agosto e setembro 2026 | 59.569,39 | Vazio | Vazio | Vazio |
| Total sem mês único | 1.975.524,68 | Vazio | Vazio | Vazio |

A consulta exibe a taxa multiplicada por 100 e arredondada a duas casas;
a medida permanente mantém a fração completa e usa formatação percentual.
A ordem das linhas é alfabética.

## Registrar após validar

Nenhuma ação no Supabase. No Source Control, preparar pelo + somente:

- definition/tables/fato_vendas.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_crescimento_mensal.dax.
- docs/crescimento_mensal_powerbi.md.

Revisar os metadados gerados ao salvar antes de incluir outros arquivos.
Deixar pendências anteriores separadas. O progresso continua local e ignorado.
Mensagem: `feat: add monthly revenue growth measures`.
Fazer Commit e depois ... → Push manualmente após revisão.
