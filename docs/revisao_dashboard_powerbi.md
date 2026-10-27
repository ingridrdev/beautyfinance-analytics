# Revisão geral do dashboard

Data: 20/10/2026. Estado: revisão dos arquivos e dos totais concluída;
correção visual do orçamento confirmada no Desktop. A conferência completa
de interações e de anos históricos ainda não foi apresentada.
Não considerar o dashboard inteiramente revisado apenas por esses testes locais.

## Escopo e resultado

Foram lidos os arquivos atuais, os guias e as evidências apresentadas pela
usuária. Não foram recriados dados, instaladas dependências ou executados
scripts de geração. Não houve conexão ao Supabase nem execução local do
motor DAX. A revisão dos valores usa as saídas do Desktop já apresentadas
e agregações independentes dos CSVs, sem exibir linhas da base de vendas.

| Página | Elementos | Evidência no Desktop | Commit original |
|---|---:|---|---|
| Visão Executiva | 20 | Captura inicial e confirmação dos filtros de mês/canal | ebba3dc |
| Produtos e Marcas | 18 | Captura, filtros de produto/mês e seis cenários DAX | 96f8942 |
| Canais e Regiões | 19 | Capturas, filtros combinados e seis cenários DAX | 58ac9b8 |
| Orçamento x Realizado | 18 | Confirmação verbal dos testes e captura de Supermercados; sem saída DAX completa recebida | 906f613 |
| Forecast | 14 | Capturas, nove cenários DAX e barras vermelhas confirmadas | 99e04a7 |

São 89 elementos nas cinco páginas. O modelo possui sete tabelas importadas,
21 medidas e nove relacionamentos. As etapas registradas não precisam ser
refeitas para retomar o projeto. Os guias das páginas foram atualizados para
informar os commits, pois alguns ainda indicavam registro pendente.

## Verificações locais que passaram

- Ordem e nomes das cinco páginas, arquivos existentes e nomes únicos.
- Campos e medidas usados por gráficos, cartões e filtros existem no modelo.
- Referências dos nove relacionamentos existem; sem relação direta entre fatos
  ou relação de forecast com produto, canal ou região.
- Elementos dentro de 1920 x 1080, sem sobreposição geométrica.
- Origens e destinos das interações apontam para visuais existentes.
- Quatro páginas de realizado limitadas a agosto/2026; Forecast limitado
  separadamente a setembro-dezembro/2026.
- Seleções salvas sem restrições adicionais, mantendo 2026 nas páginas
  de realizado. Forecast abre com os meses previstos sem seleção adicional.
- Estrutura de 83 arquivos JSON validada pelo schema exato em cache.
  Outros 12 visuais que o Desktop marcou como versão 2.14 foram comparados
  com o schema publicado 2.7, numa cópia em memória, sem alterar os arquivos.
  Isso confere compatibilidade com a estrutura antiga, não valida o schema
  nativo 2.14, cujo endereço retornou 404 nas consultas anteriores.
- Totais recalculados por leitura sequencial dos CSVs, com Decimal.

| Referência | Valor |
|---|---:|
| Linhas de vendas | 22.734 |
| Linhas de orçamento | 9.828 |
| Pedidos distintos no histórico | 15.000 |
| Unidades no histórico | 31.337 |
| Receita histórica até agosto/2026 | 1.975.524,68 |
| Custo histórico até agosto/2026 | 784.832,92 |
| Receita de janeiro a agosto/2026 | 497.957,18 |
| Orçamento comparável de janeiro a agosto/2026 | 479.918,23 |
| Previsão de setembro a dezembro/2026 | 317.686,24 |
| Orçamento de setembro a dezembro/2026 | 339.334,73 |

Essas verificações não confirmam cliques, renderização ou atualização do banco.
Não houve alteração em medidas, relações ou dados nesta revisão. Após a
captura do orçamento, a formatação de um gráfico foi corrigida conforme abaixo.

## Pontos a conferir antes de apresentar

1. **Cor da diferença mensal do orçamento.** A captura com Supermercados
   confirmou os quatro cartões e as barras negativas azuis. Com o Desktop
   fechado, ba_month_variance foi corrigido para aplicar a regra a cada mês:
   positivo verde, negativo vermelho e zero cinza. O seletor agora corresponde
   às instâncias do gráfico, em vez de somente à série. Schema e regras dos
   três sinais passaram localmente. A consulta e os cálculos foram preservados.
   Duas novas capturas confirmaram a renderização: Supermercados com barras
   vermelhas e -3.679,82 (-4,80%); todos os canais com barras verdes e
   +18.038,95 (+3,76%). Realizado e orçamento foram preservados. Zero foi
   verificado apenas na lógica local, sem cenário de valor zero apresentado.
2. **Interações e histórico.** Foram testados filtros importantes, mas ainda
   faltam evidências de seleção por clique nas barras e troca de anos. Um
   arquivo de interação válido não prova que a experiência visual funciona.
3. **Legibilidade.** Algumas capturas mostram subtítulos automáticos longos
   com nomes das medidas e trechos cortados. Os principais títulos e valores
   são visíveis, mas vale simplificar esses subtítulos numa tarefa visual própria.
   Avaliar também o tamanho dos textos no modo de leitura/apresentação.
4. **Apresentação do portfólio.** O README ainda é introdutório e informa
   análises previstas. Precisa de atualização própria com resultados, método,
   imagens e instruções; esta revisão não reescreveu o portfólio.

Após as duas capturas, a usuária salvou com Ano 2026 e filtros em Todos e
fechou o Desktop. Não foi repetido DAX, pois só a cor foi modificada.
A correção e a documentação estão prontas para revisão e registro. Os pontos
de interações/histórico e legibilidade acima continuam como próximos itens;
não foram considerados concluídos por esta conferência de cores.

Referência técnica do seletor e das regras:
[exemplo de formatação condicional da Microsoft](https://github.com/microsoft/skills-for-fabric/blob/main/skills/powerbi-report-cli/references/authoring/conditional-formatting-part-05.md).

## Pendências do Git revisadas

| Arquivo ou grupo | O que foi encontrado | Tratamento nesta revisão |
|---|---|---|
| .gitignore | Sinalizado, sem diferença de conteúdo | Preservado, separado |
| docs/relacionamentos_powerbi.md | Tinha um espaço no fim da linha e instruções antigas | Atualizado por solicitação da usuária, com validações e proteção do forecast atuais |
| 19 JSONs de Orçamento x Realizado | Inicialmente somente remoção da quebra de linha final | Apenas ba_month_variance ganhou ajuste funcional de formatação nesta revisão; demais preservados |
| docs/image.png | Captura do Forecast com barras vermelhas, incluindo interface e um subtítulo cortado | Inspecionada e preservada; revisar nome/recorte numa tarefa de imagens |

Nenhum arquivo pendente foi apagado ou revertido. Não incluir todas as
pendências automaticamente num commit. O guia de progresso segue ignorado.

## Arquivos desta revisão e próximos passos

Criado este relatório, atualizados os cinco guias das páginas com seus
commits e atualizado relacionamentos_powerbi.md por solicitação da usuária.
Corrigida a formatação de ba_month_variance e atualizado o progresso local.
Os demais arquivos pendentes continuam preservados. Nenhum commit/push executado.

Conferência de cores concluída. Registrar somente os sete documentos desta
revisão e o visual ba_month_variance. Outros JSONs com mudança de quebra de
linha, pages.json e imagens ficam separados. Não alterar o Supabase.

Mensagem sugerida para o registro da revisão, após concluí-la:
fix: correct budget variance colors and update dashboard review

## Atualização de 27/10/2026 — interações e histórico

A usuária confirmou no Desktop os testes orientados nas cinco páginas.
Em Orçamento x Realizado, as capturas mostraram janeiro/2026 selecionado,
o retorno ao total de 2026 e a seleção de 2025 com os 12 meses em ordem.
A conferência de 2024 foi confirmada por texto. Visão Executiva e Produtos
e Marcas: confirmação textual de seleção de barras, limpeza e anos 2025/2024.
Canais e Regiões: confirmação textual de cliques por canal/região, limpeza
e anos históricos. Forecast: confirmação textual do filtro de setembro,
retorno aos quatro meses, clique mensal e total de 317.686,24, com diferença
de -21.648,49 (-6,38%). Não foram recebidas capturas desses últimos testes
nem novas saídas DAX; a evidência é a confirmação da usuária.

A revisão anterior foi registrada e enviada no commit 4c2d085.
Os itens de interações e histórico acima deixam de ser pendentes nos cenários
orientados. Próximo passo: melhorar a legibilidade dos subtítulos automáticos
longos. Em 27/10, o processo PBIDesktop ainda estava aberto; salvar e fechar
normalmente antes de editar os arquivos do relatório. Não foi fechado pelo agente.
Esta atualização documental ainda não foi registrada em novo commit.

## Ajuste de legibilidade em 27/10/2026

Após confirmação do fechamento e consulta sem processo PBIDesktop, os 16
gráficos das cinco páginas receberam visualContainerObjects.subTitle.show=false.
O tema Fluent2 habilitava subtítulos automáticos, exibindo nomes extensos de
campos, inclusive tooltips. Os títulos descritivos foram preservados.
Comparação estrutural em memória verificou que a inserção só adicionou essa
propriedade; todos os JSONs das páginas foram lidos e os 16 valores conferidos.
Não houve alteração de consultas, medidas, relações, títulos ou cores pelo
ajuste. Alterações geradas pelo Desktop antes desta edição foram preservadas.
Próximo passo: reabrir o PBIP e conferir a renderização nas cinco páginas.
Sem nova validação de schema ou renderização nesta etapa; sem commit/push.

### Conferência visual após salvar

A captura de Orçamento x Realizado confirmou os quatro gráficos sem os
subtítulos automáticos, com títulos, valores e cores preservados. A usuária
informou que salvou e fechou; a consulta de processos confirmou o fechamento.
Os 16 gráficos preservam subTitle.show=false após salvar. Não foram recebidas
capturas das outras quatro páginas para este ajuste visual.
O registro desta etapa inclui apenas a propriedade dos subtítulos e este
documento; demais alterações do Desktop permanecem separadas.

## Capturas atuais conferidas em 27/10/2026

As cinco imagens de docs/images foram inspecionadas visualmente: Visão
Executiva, Produtos e Marcas, Canais e Regiões, Orçamento x Realizado e Forecast.
As quatro páginas de realizado mostram Ano 2026 e demais filtros em Todos,
sem seleção de barras visível. Indicadores de 2026 coincidem com os valores
já documentados. Forecast mostra os quatro meses, filtro Todos, previsão de
317.686,24, orçamento de 339.334,73 e diferença de -21.648,49 (-6,38%).
Os gráficos estão sem os subtítulos automáticos longos. A captura final do
Forecast também está sem a borda de seleção do título. Essas imagens
complementam a conferência visual das cinco páginas após o ajuste; não
representam uma nova execução das consultas DAX. README atualizado com a
galeria completa, substituindo a indicação de captura histórica.
