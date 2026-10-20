# Orçamento x Realizado — primeira versão

Implementada em 20/10/2026. A usuária confirmou que os testes solicitados
estavam corretos e depois salvou e fechou o Power BI. Validação local
concluída; arquivos aguardam revisão e registro no GitHub.

## Página e regras

A quarta página compara receita realizada e orçamento no mesmo período.
Tem seis filtros (ano, meses, marca, categoria, canal e região), quatro
cartões (realizado, orçamento comparável, diferença em reais e percentual)
e quatro gráficos: comparação mensal, diferença mensal em percentual,
comparação por marca e comparação por categoria.

O estado inicial é 2026, com os demais filtros em Todos. O limite da página
é 31/08/2026, data final do realizado fictício. O histórico 2024/2025 continua
disponível. A página não mostra forecast nem metas de meses futuros.
As metas são mensais, representadas no primeiro dia do mês; não há filtro diário.

Realizado usa Receita Líquida. Todos os comparativos visuais usam Receita
Orçada Comparável. Diferença = realizado - comparável; percentual = diferença
dividida pelo comparável. Não é percentual de atingimento. Valor positivo
significa acima do orçamento de receita; negativo significa abaixo.
Sem realizado ou sem orçamento comparável, a diferença fica vazia.

O orçamento selecionado completo aparece somente no teste DAX para conferir
a exclusão dos meses futuros; não é usado como denominador dos gráficos.
O corte das medidas vem da base, enquanto o limite visual é fixo da simulação.
Se o período da base mudar, revisar também o limite da página em tarefa própria.

Os gráficos por marca/categoria são ordenados pela receita realizada; meses
estão em ordem cronológica. Os cartões de diferença usam sinal e cores.
A diferença mensal também tem sinal e eixo zero; a cor condicional precisa
de conferência no Desktop, pois schema válido não comprova renderização.

Clicar nas barras foi configurado para filtrar gráficos e cartões.
Os gráficos não restringem as listas dos filtros; ano restringe meses.

## Validação local

- 20 JSONs (18 visuais, página e ordem) passaram nos schemas oficiais da
  Microsoft consultados anteriormente e mantidos em cache temporário.
- Nomes, referências ao modelo, interações, limites e ausência de
  sobreposição dos elementos conferidos.
- Agregações por mês, marca e categoria coincidem com os totais dos CSVs.
- Dinheiro calculado com Decimal por leitura sequencial, sem alterar bases.
- Oito recortes conferidos, incluindo Supermercados abaixo da meta, setembro
  sem realizado e agosto+setembro com somente agosto comparável.
- Consulta 1 idêntica a powerbi/validar_orcamento_realizado.dax.
- Nenhuma medida, tabela, relação ou fonte foi alterada. As três páginas
  anteriores foram preservadas. Somente a lista/aba ativa e consulta salva
  foram atualizadas. O teste anterior segue em validar_canais_regioes.dax.

## Confirmação no Desktop

A usuária respondeu "tudo certo" após receber as instruções para conferir
a página inicial, Supermercados abaixo da meta, Lumera acima da meta e
executar a consulta de oito cenários. Essa confirmação foi registrada sem
receber captura da página nem os resultados DAX completos nesta etapa.
Os valores da tabela abaixo são referências calculadas dos CSVs, não uma
transcrição de saída do Desktop. A aparência e as cores não foram inspecionadas
diretamente; os cliques nas barras também não foram apresentados.

## Conferência no Desktop

1. Abra powerbi/beauty_analytics.pbip, clique em Atualizar e abra Orçamento x Realizado.
2. Envie uma captura inicial. Os quatro cartões devem coincidir com Jan-ago 2026.
3. Selecione Supermercados em Canal: a diferença precisa ser negativa. Confira o sinal
   e a cor nos cartões e no gráfico mensal.
4. Limpe Canal e selecione Marca Lumera. Confira a referência abaixo.
5. Execute Consulta 1 na Exibição de consulta DAX e envie as oito linhas.
   Essa consulta inclui setembro e agosto+setembro fora do filtro fixo da página.
6. Confira se selecionar uma marca no gráfico altera os indicadores.
7. Restaure Ano 2026 e demais filtros em Todos. Salve com Ctrl + S.
   Mantenha aberto durante a revisão e feche antes de novas edições externas.

| Cenário | Realizado | Orçamento selecionado | Comparável | Diferença R$ | Diferença % |
|---|---:|---:|---:|---:|---:|
| Jan-ago 2026 | 497957.18 | 479918.23 | 479918.23 | 18038.95 | 3.76 |
| Supermercados 2026 | 72922.19 | 76602.01 | 76602.01 | -3679.82 | -4.80 |
| Agosto 2026 | 59569.39 | 57792.52 | 57792.52 | 1776.87 | 3.07 |
| Marca Lumera 2026 | 124171.45 | 119808.51 | 119808.51 | 4362.94 | 3.64 |
| Categoria Pele 2026 | 167722.91 | 161692.85 | 161692.85 | 6030.06 | 3.73 |
| E-commerce Sudeste 2026 | 61148.54 | 52593.57 | 52593.57 | 8554.97 | 16.27 |
| Setembro 2026 sem realizado | Vazio | 67982.82 | Vazio | Vazio | Vazio |
| Agosto e setembro 2026 | 59569.39 | 125775.34 | 57792.52 | 1776.87 | 3.07 |

## Arquivos e registro

Arquivos desta etapa: pasta bf_orcamento_realizado (page.json e 18 visual.json),
pages.json, Consulta 1.dax, powerbi/validar_orcamento_realizado.dax e este guia.
Documento local de progresso segue ignorado. .gitignore permanece separado.
Revisar eventuais arquivos adicionais gerados pelo Desktop ao salvar.

Nenhuma ação necessária no Supabase. Validar, salvar e fechar antes da revisão
para registro no GitHub. Nenhum commit/push foi feito nesta etapa.
Mensagem sugerida: feat: add budget versus actual analysis page

Referência: [PBIR — Microsoft Learn](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-report).
