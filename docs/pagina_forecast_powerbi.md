# Forecast de Receita — primeira versão

Implementada em 20/10/2026. Os nove cenários DAX foram executados no Desktop
e coincidiram com as referências. As capturas confirmaram os quatro cartões,
os valores mensais, os textos e a abertura da página. Foi identificado um
ajuste visual nas barras de diferença; a nova captura confirmou as quatro
barras vermelhas, com valores preservados. A usuária salvou e fechou o Desktop;
a revisão confirmou vermelho preservado, meses sem seleção e testes iguais.
A etapa aguarda autorização para registro no GitHub.

## Conteúdo e limites

A quinta página tem 14 elementos: sete textos, um filtro de meses, quatro
cartões e dois gráficos. Os cartões usam as quatro medidas existentes da
vw_forecast_receita: previsão, orçamento do período previsto, diferença
em reais e percentual. Os gráficos comparam previsão e orçamento por mês
e apresentam a diferença mensal em reais, com sinais e cores.

O filtro fixo limita o calendário a setembro-dezembro/2026, sem herdar o
corte de agosto das páginas de realizado. O filtro de meses inicia em Todos
e deve oferecer apenas os quatro meses previstos. Não há filtros de produto,
marca, categoria, canal ou região. As medidas existentes retornam vazio
quando recebem esses filtros, pois a previsão não possui esse detalhamento.
Não há crescimento ou filtro de ano novo no modelo.

A comparação usa Orçamento Período Forecast, nunca Receita Orçada Comparável.
Esta última é limitada ao realizado e não serve para comparar meses futuros.
Diferença = previsão - orçamento dos mesmos meses; a taxa divide a diferença
pelo orçamento total selecionado, sem média de percentuais mensais.

## Método e interpretação

Repete a regra de sql/08_criar_view_forecast.sql: divide a receita de
jan-ago/2026 pela de jan-ago/2025 e aplica o fator sem arredondamento
a cada receita de set-dez/2025. Arredonda cada previsão mensal a centavos
e soma os meses arredondados. O crescimento exibido é 7,66%.
O método mantém o padrão de fim de ano de 2025 e pressupõe continuidade
do crescimento recente. Não garante resultados e não fornece intervalo
de incerteza. Não prevê custo ou margem.

O total previsto é 317.686,24 contra orçamento de 339.334,73: diferença
-21.648,49 (-6,38%). A receita realizada até agosto não está incluída nesse
total. Ele representa apenas os quatro meses previstos, não o ano inteiro.
A diferença percentual semelhante nos quatro meses decorre do método de
previsão e da regra do orçamento; não são quatro taxas independentes.

## Validação local

- 16 JSONs (14 visuais, página e lista de páginas) passaram nos schemas
  oficiais da Microsoft previamente consultados e mantidos em cache.
- Nomes, referências, posições, interações e ausência de sobreposição conferidos.
- Previsões recalculadas dos CSVs com Decimal, sem arredondar o fator antes
  da aplicação. Os quatro valores coincidem com os resultados SQL já validados.
- Orçamento mensal agregado dos CSVs; total e diferenças conferem.
- Consulta 1 idêntica a powerbi/validar_pagina_forecast.dax.
- Nenhuma medida, relação, tabela, fonte ou SQL foi alterado.
- As quatro páginas anteriores foram preservadas. Somente a ordem/aba ativa
  e a consulta salva foram atualizadas; validar_orcamento_realizado.dax permanece.

Os filtros sem detalhamento foram conferidos pela consulta DAX no Desktop,
sem novos filtros visuais. Não houve execução local do motor DAX. Os schemas confirmam
a estrutura, mas não substituem os testes no Desktop nem comprovam cores.

## Conferência recebida e ajuste visual

A saída DAX enviada pela usuária confirmou os quatro meses e o total:
317.686,24 de previsão, 339.334,73 de orçamento e -21.648,49 de diferença.
Agosto e os filtros de marca/canal/região retornaram vazio como esperado.
As taxas mensais e total arredondam para -6,38%; pequenas diferenças nas
casas adicionais decorrem dos valores monetários arredondados por mês.

Nas capturas, os cartões de diferença ficaram vermelhos, mas as barras
continuaram azuis: a propriedade condicional da série não foi aplicada
pelo visual. Após salvar e fechar, foi configurada a cor padrão vermelha
no gráfico fc_month_variance. Os quatro resultados atuais são negativos,
inclusive qualquer soma dos meses selecionados. Essa cor é fixa para o
cenário atual; se a base ou método mudar e produzir valores positivos,
revisar a formatação. Não houve mudança nos cálculos ou dados.
A nova cor passou na validação de schema e foi confirmada em captura do Desktop.
Seleção mensal e cliques nas colunas não foram apresentados nesta revisão.

## Conferir no Desktop

1. Abra powerbi/beauty_analytics.pbip, clique em Atualizar e abra Forecast.
2. Envie uma captura inicial. Confira os quatro cartões com Total forecast.
3. Em Meses previstos, confira se há apenas setembro a dezembro/2026.
4. Selecione 2026-09: previsto 63.645,73, orçamento 67.982,82 e diferença
   -4.337,09 (-6,38%). Confira também sinal e cor dos cartões/gráfico.
5. Execute Consulta 1 na Exibição de consulta DAX e envie as nove linhas.
6. Teste clicar em uma coluna mensal e confira os cartões do mesmo mês.
7. Restaure Meses previstos em Todos e limpe seleções nos gráficos.
   Salve com Ctrl + S. Mantenha aberto durante a revisão; feche antes
   de novas edições externas.

| Cenário | Previsão | Orçamento | Diferença R$ | Diferença % |
|---|---:|---:|---:|---:|
| Total forecast | 317686.24 | 339334.73 | -21648.49 | -6.38 |
| 2026-09 | 63645.73 | 67982.82 | -4337.09 | -6.38 |
| 2026-10 | 64403.80 | 68792.62 | -4388.82 | -6.38 |
| 2026-11 | 90927.21 | 97123.34 | -6196.13 | -6.38 |
| 2026-12 | 98709.50 | 105435.95 | -6726.45 | -6.38 |
| Agosto sem forecast | Vazio | Vazio | Vazio | Vazio |
| Marca sem detalhamento | Vazio | Vazio | Vazio | Vazio |
| Canal sem detalhamento | Vazio | Vazio | Vazio | Vazio |
| Região sem detalhamento | Vazio | Vazio | Vazio | Vazio |

## Arquivos e registro

Arquivos: pasta bf_forecast (page.json e 14 visual.json), pages.json,
Consulta 1.dax, powerbi/validar_pagina_forecast.dax e este documento.
O progresso local continua ignorado e .gitignore permanece separado.
Revisar eventuais metadados que o Desktop alterar ao salvar.
O Desktop acrescentou nomes auxiliares dos campos em cultures/pt-BR.tmdl.
Arquivos da página anterior Orçamento x Realizado também apareceram como
modificados por remoção da quebra de linha final; revisar separadamente
e não incluir automaticamente no commit do Forecast.

Nenhuma ação necessária no Supabase: a view já existe e não foi alterada.
Após validar, salvar e fechar antes da revisão para registro no GitHub.
Mensagem sugerida: feat: add revenue forecast analysis page
Nenhum commit/push feito nesta etapa.

Referência: [PBIR — Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report).
