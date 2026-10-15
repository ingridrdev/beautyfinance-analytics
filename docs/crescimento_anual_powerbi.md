# Crescimento anual da receita por mês (YoY)

## Medidas

Três medidas em fato_vendas, na pasta Crescimento anual:

- Receita Mesmo Mês Ano Anterior: usa DATEADD com deslocamento de um ano.
- Variação Receita YoY: receita atual menos a receita do mesmo mês anterior.
- Crescimento Receita YoY %: diferença dividida pela receita anterior.

Este YoY compara meses: agosto de 2026 com agosto de 2025. Não representa
comparação de anos completos ou de acumulados. Os filtros de produto,
canal e região permanecem aplicados. Usar ano_mes de dim_calendario.

A comparação exige um único mês completo, com realizado atual e base
anterior. Sem histórico de 2023, os meses de 2024 não têm comparação.
Meses futuros, totais de vários meses e seleção de dias parciais retornam
vazio nas três medidas YoY. DIVIDE protege a divisão por zero.
O percentual é uma fração formatada, sem multiplicação por 100 na medida.

## Testes locais

Receitas mensais recalculadas com Decimal; 20 pares anuais disponíveis.
Foram verificadas as referências para queda, crescimento, fevereiro em
comparação com 2024 bissexto, canal, ausência de base e ausência de vendas.
A consulta salva corresponde ao teste independente. As medidas e testes
anteriores foram preservados. Não foi executado o motor DAX nesta etapa local.

## Reabrir e executar

1. Abra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Abra Exibição de consulta DAX → Consulta 1.
3. Clique em Executar. O teste já está colocado; não copiar código.
4. Envie as dez linhas para conferir antes do commit.
5. Após a validação, salve com Ctrl + S. Feche antes da próxima edição
   externa e reabra para novos testes, conforme orientação.

Resultados esperados (a ordem de apresentação é alfabética):

| Cenário | Atual | Mesmo mês anterior | Variação | YoY % |
|---|---:|---:|---:|---:|
| Agosto 2024 sem histórico | 54.646,54 | Vazio | Vazio | Vazio |
| Janeiro 2025 | 52.378,90 | 56.985,04 | -4.606,14 | -8,08 |
| Fevereiro 2025 | 52.899,11 | 49.487,52 | 3.411,59 | 6,89 |
| Julho 2026 | 56.825,11 | 59.923,81 | -3.098,70 | -5,17 |
| Agosto 2026 | 59.569,39 | 59.096,92 | 472,47 | 0,80 |
| Canal 1 agosto 2026 | 15.262,98 | 16.528,65 | -1.265,67 | -7,66 |
| Setembro 2026 sem realizado | Vazio | Vazio | Vazio | Vazio |
| Ano 2026 sem mês único | 497.957,18 | Vazio | Vazio | Vazio |
| Agosto 2026 dias 1 a 15 | 28.927,20 | Vazio | Vazio | Vazio |
| Total sem mês único | 1.975.524,68 | Vazio | Vazio | Vazio |

O teste também está em powerbi/validar_crescimento_anual.dax. Ele arredonda
e multiplica a taxa por 100 somente para apresentar a referência.
Fevereiro testa a seleção de todo o mês anterior, incluindo 29/02/2024.
Se houver diferença, investigar antes de alterar a referência ou a medida.

## Registro

Nenhuma ação no Supabase. Após conferir e salvar, preparar no Source Control:

- definition/tables/fato_vendas.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_crescimento_anual.dax.
- docs/crescimento_anual_powerbi.md.

Revisar os metadados adicionais antes de incluir. Não incluir pendências
anteriores automaticamente. O documento de progresso continua local e ignorado.
Mensagem: `feat: add yearly revenue growth measures`.
Fazer Commit e depois ... → Push manualmente, aguardando revisão.
