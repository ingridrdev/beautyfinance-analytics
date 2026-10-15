# Medidas de receita orçada versus realizada

## Medidas criadas

Quatro medidas em fato_orcamento, na pasta Orçamento e realizado:

| Medida | Função |
|---|---|
| Receita Orçada | Meta de todo o período selecionado, incluindo futuro |
| Receita Orçada Comparável | Meta selecionada até o último mês com vendas na base |
| Variação Receita Orçamento | Receita líquida menos orçamento comparável |
| Variação Receita Orçamento % | Variação dividida pelo orçamento comparável |

O total das vendas termina em agosto de 2026. Compará-lo com o orçamento
até dezembro de 2026 incluiria metas de quatro meses ainda sem realizado.
Por isso as variações usam sempre o orçamento comparável.

O corte vem da maior data de fato_vendas, sem filtros, e vai até o fim
daquele mês. Ele não depende da data real do computador nem do canal,
produto ou mês selecionado. Na base atual, o corte é agosto de 2026.
Os filtros do usuário continuam aplicados ao cálculo do orçamento;
KEEPFILTERS mantém sua interseção com o limite de data.
Fonte: [KEEPFILTERS](https://learn.microsoft.com/en-us/dax/keepfilters-function-dax).

Se não houver realizado ou orçamento comparável, a diferença fica vazia.
DIVIDE protege a divisão por zero. A medida percentual armazena uma fração;
a consulta de teste multiplica por 100 apenas para facilitar a leitura.

## Limites

Usar os campos de dim_calendario para filtrar períodos e os campos das
dimensões para produto/canal/região. Os valores do orçamento são mensais,
representados pelo primeiro dia; não há distribuição diária.

O cálculo considera o último mês com vendas como realizado disponível.
Se a base passar a ter meses incompletos, será necessário definir outro
controle de fechamento antes de aplicar o método. Se o corte da simulação
mudar, forecast e documentação também precisarão de revisão própria.

Um recorte sem vendas retorna vazio; não significa automaticamente que
houve faturamento zero. O status de meses futuros não deve ser apresentado
como resultado abaixo do orçamento. Não foram criadas medidas de custo
orçado, margem orçada ou forecast nesta tarefa.

## Validação

Os totais e recortes foram recalculados a partir dos CSVs com Decimal.
Foram conferidos: total, ano 2026, canal 1, agosto, setembro sem realizado
e seleção conjunta de agosto/setembro. O último cenário mantém somente
agosto na comparação, preservando a meta de ambos na medida completa.
As fórmulas e referências foram inspecionadas. O motor DAX ainda não foi
executado nesta validação local.

Resultados esperados no teste:

| Cenário | Realizado | Orçamento selecionado | Comparável | Variação | Variação % |
|---|---:|---:|---:|---:|---:|
| Total | 1.975.524,68 | 2.245.554,82 | 1.906.220,09 | 69.304,59 | 3,64 |
| Ano 2026 | 497.957,18 | 819.252,96 | 479.918,23 | 18.038,95 | 3,76 |
| Canal 1 | 545.089,65 | 582.170,03 | 489.217,22 | 55.872,43 | 11,42 |
| Agosto 2026 | 59.569,39 | 57.792,52 | 57.792,52 | 1.776,87 | 3,07 |
| Setembro 2026 sem realizado | Vazio | 67.982,82 | Vazio | Vazio | Vazio |
| Agosto e setembro 2026 | 59.569,39 | 125.775,34 | 57.792,52 | 1.776,87 | 3,07 |

## Ações manuais

1. Reabra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Abra Exibição de consulta DAX → Consulta 1. O teste já está colocado.
3. Clique em Executar e envie as seis linhas para conferir.
4. Após a conferência, salve com Ctrl + S. Feche antes da próxima edição
   externa do modelo e reabra para novos testes, conforme orientação.

O teste também está em powerbi/validar_medidas_orcamento.dax. Os anteriores
foram preservados. Nenhum SQL novo deve ser executado no Supabase.

Após validar, prepare no Source Control somente:

- definition/tables/fato_orcamento.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_medidas_orcamento.dax.
- docs/medidas_orcamento_powerbi.md.

Revise separadamente eventuais arquivos de metadados alterados ao salvar.
O documento de progresso continua local e ignorado. Não incluir pendências
anteriores automaticamente. Mensagem sugerida:
`feat: add comparable revenue budget measures`.
Faça Commit e depois ... → Push manualmente após a revisão.
