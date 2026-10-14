# BeautyFinance Analytics — continuidade do projeto

Atualizado em: 13/10/2026.

Este documento registra onde o projeto parou, o que já foi feito e como
retomar o trabalho sem depender de uma conversa anterior. Leia este arquivo
e confira os arquivos atuais antes de implementar algo. Não refaça etapas
concluídas apenas para retomar o contexto.

## 1. Ponto exato para retomar

O projeto Power BI foi salvo em formato **PBIP** e suas sete importações
foram configuradas nos arquivos. Esse trabalho já está no GitHub, no commit
`1cd9f68`.

**Próxima tarefa única: confirmar a atualização e a carga das sete tabelas
no Power BI Desktop, sem erros, e conferir suas quantidades de linhas.**

A usuária informou que salvou as tabelas. Isso não é evidência suficiente
para concluir que a carga completa terminou corretamente. Ainda não foram
apresentadas as contagens ou os totais calculados no Power BI após a mudança.
Não registrar essa validação como concluída antes de conferi-la.

Passos para essa próxima tarefa:

1. Abrir `powerbi/beauty_analytics.pbip` no Power BI Desktop.
2. Clicar em **Página Inicial → Atualizar** e aguardar terminar.
3. Se necessário, informar as credenciais atuais na janela do aplicativo.
4. Conferir as sete tabelas e as quantidades indicadas na seção 4.
5. Se aparecer erro, guardar o texto e investigar antes de prosseguir.
6. Salvar o projeto após a carga bem-sucedida.

Nenhum SQL novo precisa ser executado para essa conferência. Só depois
dessa validação será iniciada outra tarefa, como os relacionamentos.

## 2. Objetivo e regras de trabalho

Projeto educacional e de portfólio de análise financeira e comercial de
uma empresa fictícia de cosméticos, com foco em vendas, custos, margem,
orçamento, crescimento e previsão de receita.

A usuária está no primeiro período de Análise e Desenvolvimento de Sistemas.
Explicar tudo em português, com linguagem simples e exemplos quando úteis.

Regras permanentes:

- Trabalhar em uma tarefa por vez e explicar primeiro o que será feito.
- Preservar alterações existentes e não refazer etapas concluídas.
- Editar e executar arquivos dentro do escopo autorizado pela usuária.
- Não apagar arquivos ou dados sem autorização.
- Validar cada mudança; distinguir teste local de execução no banco ou no Power BI.
- Não inventar resultados nem considerar uma etapa validada só porque foi salva.
- Após cada tarefa, informar arquivos modificados, mudanças, testes e limitações.
- Explicar as ações manuais necessárias, em ordem, incluindo Supabase e Git.
- Colocar apenas comandos executáveis nos blocos copiáveis; resultados esperados ficam fora.
- Aguardar revisão antes de passar para a próxima tarefa.
- Antes de editar o PBIP, pedir que a usuária salve e feche o Power BI
  para evitar sobreposição de gravações, como combinado nesta etapa.

### Git e GitHub ficam sob controle da usuária

Repositório: https://github.com/ingridrdev/beautyfinance-analytics

Quem dá continuidade pode usar apenas comandos Git de consulta, como
`git status`, `git diff` e `git log`.

Não executar `git add`, `git commit`, `git push`, `git pull`, criar branches
ou Pull Requests, alterar configurações do Git ou desfazer alterações.
A usuária fará os registros manualmente, preferindo a interface
**Source Control (Controle do Código-Fonte) do VS Code**, em vez do terminal.
As mensagens dos novos commits devem ser **em inglês**; as explicações e
a documentação continuam em português. Não reescrever commits antigos
apenas para traduzir suas mensagens.

Fluxo preferido na interface:

1. Abrir Source Control e clicar no arquivo para revisar as diferenças.
2. Clicar no **+** somente nos arquivos da tarefa para prepará-los.
3. Conferir a lista **Staged Changes** (Alterações Preparadas).
4. Digitar a mensagem de commit em inglês e clicar em **Commit**.
5. No menu **...**, escolher **Push** para enviar os commits.

Evitar **Stage All** quando existirem alterações de outras tarefas.
Preferir **Push** a **Sync Changes**: a sincronização pode também buscar
e incorporar mudanças remotas. Se houver erro, conferir a mensagem antes
de escolher outra ação.

Não adicionar assinaturas automáticas, `Co-authored-by` ou comentários
de autoria automática. Nunca incluir senhas, chaves ou credenciais nos
arquivos ou no GitHub. Digitar a senha somente na autenticação apropriada.

No terminal, preferir `git --no-pager diff` para evitar o visualizador
interativo, que já causou confusão. Os avisos LF/CRLF são sobre quebras de
linha do Windows; isoladamente, não indicam falha de commit.

Ordem de registro: conferir alterações, validar, selecionar arquivos com
`git add`, revisar com `git --no-pager diff --cached`, criar `git commit` e
então executar `git push`. Salvar no Power BI não cria commit. Um push sem
commit novo não envia alterações dos arquivos. O push também não executa
SQL nem cria views no Supabase.

## 3. Organização e caminho dos dados

| Local | Conteúdo |
|---|---|
| `data/raw` | Dimensões, calendário, vendas brutas e orçamento gerado |
| `data/processed` | Vendas tratadas, qualidade, validações e resumos |
| `src` | Scripts Python de geração, tratamento e validação |
| `sql` | Tabelas, views, validação e análises financeiras |
| `docs` | Planejamento, dicionário, conexão e este documento |
| `powerbi` | Projeto PBIP, modelo e definição do relatório |
| `excel` | Reservada para análises complementares futuras |
| `README.md` | Apresentação principal, ainda resumida |
| `requirements.txt` | Dependências Python |
| `.gitignore` | Exclusões do controle de versão |

Fluxo já implementado:

1. `src/gerar_dimensoes.py`: produtos, canais e regiões.
2. `src/gerar_calendario.py`: datas e atributos do calendário.
3. `src/gerar_vendas.py`: vendas fictícias e problemas controlados de qualidade.
4. `src/tratar_vendas.py`: remove duplicidades, preenche descontos e calcula métricas.
5. `src/gerar_orcamento.py`: gera metas mensais.
6. `src/validar_dados.py`: valida dados e salva relatórios e resumos.
7. CSVs carregados manualmente nas seis tabelas PostgreSQL do Supabase.
8. Views e consultas SQL analisam os dados.
9. Power BI conecta ao banco; importações configuradas, carga final pendente de conferência.

Os scripts Python já foram executados. Não os executar novamente apenas
para retomar o projeto: eles podem sobrescrever CSVs.

## 4. Períodos e quantidades de referência

- Histórico: janeiro de 2024 a dezembro de 2025.
- Realizado mais recente da simulação: janeiro a agosto de 2026.
- Orçamento: janeiro de 2024 a dezembro de 2026.
- Forecast: setembro a dezembro de 2026.

Setembro a dezembro de 2026 têm orçamento e previsão, mas não realizado.
O corte da simulação permanece agosto de 2026, independentemente da data
real do computador. Meses futuros não devem ser tratados como fracasso
de vendas ou queda de 100%.

| Objeto | Quantidade validada/esperada |
|---|---:|
| `dim_produtos` | 15 linhas |
| `dim_canais` | 5 linhas |
| `dim_regioes` | 5 linhas |
| `dim_calendario` | 1.096 linhas |
| `fato_vendas` | 22.734 linhas |
| `fato_orcamento` | 9.828 linhas |
| Seis tabelas somadas | 33.683 linhas |
| Pedidos distintos | 15.000 |
| Unidades vendidas | 31.337 |
| `vw_forecast_receita` | 4 linhas calculadas |

As views não são novas bases físicas de vendas. Não somar suas linhas
às tabelas como se representassem transações adicionais.

Tratamento já concluído: 22.759 linhas brutas, 25 duplicidades removidas,
60 descontos vazios preenchidos e 22.734 linhas tratadas. O relatório
registrou zero remoções pelo filtro de valores inválidos.

## 5. Indicadores já validados em Python e SQL

Valores para todo o realizado, de janeiro de 2024 a agosto de 2026:

| Indicador | Valor |
|---|---:|
| Receita líquida | R$ 1.975.524,68 |
| Custo total | R$ 784.832,92 |
| Margem bruta | R$ 1.190.691,76 |
| Margem percentual | 60,27% |
| Pedidos distintos | 15.000 |
| Ticket médio | R$ 131,70 |
| Receita orçada no período comparável | R$ 1.906.220,09 |
| Diferença de receita sobre orçamento | R$ 69.304,59 |
| Variação sobre orçamento | 3,64% |

Os arquivos `validacao_dados.csv` e `resumo_executivo.csv` guardam essas
referências. As verificações salvas apresentam status OK para duplicidade,
valores obrigatórios, dimensões, período e cálculo da margem.

Margem percentual agregada deve ser calculada como margem total dividida
pela receita total, não como média simples dos percentuais das linhas.
Ticket médio usa receita dividida por pedidos distintos; não somar
contagens distintas de grupos para obter pedidos totais.

## 6. Banco, views e análises SQL concluídas

| Arquivo | Etapa |
|---|---|
| `sql/01_criar_tabelas.sql` | Seis tabelas e relacionamentos do banco |
| `sql/02_validar_banco.sql` | Quantidades e indicadores da carga |
| `sql/03_criar_views.sql` | Vendas e orçamento detalhados |
| `sql/04_criar_view_budget_actual.sql` | Comparação de realizado e orçamento |
| `sql/05_consultas_analiticas.sql` | Análises comerciais, MoM e YoY |
| `sql/06_forecast_receita.sql` | Previsão e comparação com orçamento |
| `sql/07_validar_forecast_historico.sql` | Teste histórico da previsão |
| `sql/08_criar_view_forecast.sql` | View para consumo do forecast |

Views já criadas no Supabase, conforme execuções acompanhadas pela usuária:

- `public.vw_vendas_detalhadas`.
- `public.vw_orcamento_detalhado`.
- `public.vw_budget_actual`.
- `public.vw_forecast_receita`.

As views seguem o padrão `security_invoker = true`. A coluna `trimestre`
é texto, pois usa valores como T1 e T2.

O arquivo 05 contém consultas independentes separadas por comentários e
ponto e vírgula. Isso é intencional. Estão concluídas as análises por mês,
marca/categoria, orçamento por marca/categoria, produto, canal e região.

Principais achados já discutidos:

- Sérum de Vitamina C lidera em receita: R$ 228.173,15.
- Protetor Solar FPS 60 combina receita alta com menor margem percentual: 56,16%.
- Batom Matte apresenta margem de 67,72%.
- E-commerce representa 27,59% da receita.
- Supermercados apresentam margem de 61,83%; marketplace, 57,55%.
- Sudeste representa 45,37% da receita; as margens regionais são próximas.
- As combinações de marca/categoria ficaram acima do orçamento de receita,
  mas com margem percentual realizada um pouco abaixo da orçada.

Esses achados descrevem dados fictícios. Hipóteses sobre taxas ou custos
de canais não foram comprovadas por dados específicos de despesas.

### Crescimento mensal e anual

MoM compara com o mês anterior, inclusive na passagem entre anos.
YoY compara com o mesmo mês do ano anterior. As duas consultas retornam
32 meses e tiveram os resultados apresentados e conferidos no Supabase.

Janeiro de 2024 não tem comparação MoM. Todos os meses de 2024 não têm
comparação YoY, pois não há histórico de 2023. Divisões por zero são protegidas.

Agosto de 2026: receita R$ 59.569,39; crescimento MoM de 4,83%; crescimento
YoY de 0,80%. Novembro/dezembro têm peso maior na geração fictícia de vendas,
o que ajuda a explicar a sazonalidade de fim de ano.

## 7. Forecast e sua validação

Método de receita:

1. Somar janeiro a agosto de 2025: R$ 462.513,50.
2. Somar janeiro a agosto de 2026: R$ 497.957,18.
3. Dividir o total de 2026 pelo de 2025 para obter o fator de crescimento.
4. Multiplicar cada receita de setembro a dezembro de 2025 por esse fator.

O crescimento exibido é 7,66%, mas o fator completo é usado no cálculo,
antes de arredondar as previsões para centavos. Não se usa a média simples
das taxas mensais. O orçamento não entra no cálculo da previsão.

| Mês de 2026 | Forecast | Orçamento | Diferença |
|---|---:|---:|---:|
| Setembro | R$ 63.645,73 | R$ 67.982,82 | -R$ 4.337,09 |
| Outubro | R$ 64.403,80 | R$ 68.792,62 | -R$ 4.388,82 |
| Novembro | R$ 90.927,21 | R$ 97.123,34 | -R$ 6.196,13 |
| Dezembro | R$ 98.709,50 | R$ 105.435,95 | -R$ 6.726,45 |
| Total | R$ 317.686,24 | R$ 339.334,73 | -R$ 21.648,49 |

A previsão está 6,38% abaixo do orçamento. A taxa é igual entre os meses
porque orçamento e forecast usam a mesma base de meses de 2025, com fatores
diferentes. O orçamento futuro foi gerado com crescimento de receita de 15%.

Os resultados completos do arquivo 06 e da view criada pelo arquivo 08
foram enviados pela usuária e conferidos com a validação local.

Limites: previsão simples de receita total, sem estimativa de custo/margem
e sem detalhamento por produto, canal ou região. Ela pressupõe continuidade
do crescimento recente e do padrão de fim de ano. A view recalcula sobre
os dados disponíveis; não guarda uma versão histórica imutável.

### Teste histórico do arquivo 07

Simula uma previsão feita em agosto de 2025. Usa janeiro a agosto de
2024/2025 para calcular o fator e setembro a dezembro de 2024 como base.
O realizado de setembro a dezembro de 2025 é usado apenas para avaliar
o erro, sem influenciar a previsão.

| Mês de 2025 | Previsto | Realizado | Erro percentual |
|---|---:|---:|---:|
| Setembro | R$ 55.955,76 | R$ 59.115,54 | -5,35% |
| Outubro | R$ 58.420,14 | R$ 59.819,66 | -2,34% |
| Novembro | R$ 84.953,12 | R$ 84.455,18 | 0,59% |
| Dezembro | R$ 100.369,24 | R$ 91.683,54 | 9,47% |

Erro = previsto menos realizado. WAPE = soma dos erros absolutos dividida
pela soma do realizado, vezes 100. O WAPE local foi **4,66%**, repetido
nas quatro linhas da consulta. Um único teste de quatro meses não garante
o mesmo desempenho em 2026.

Limite da evidência: os cálculos foram conferidos localmente com Decimal
e SQLite em memória. A usuária informou que o Supabase retornou os quatro
meses, mas não apresentou seus valores completos para conferência.

## 8. Power BI: estado e ocorrências

Projeto principal: `powerbi/beauty_analytics.pbip`.

- `beauty_analytics.Report`: definição do relatório, ainda sem dashboard construído.
- `beauty_analytics.SemanticModel`: modelo com definições TMDL e consultas M.
- Sete objetos de importação: as seis tabelas originais e `vw_forecast_receita`.
- Não importar tabelas internas auth/vault/extensions do Supabase.
- As outras views continuam disponíveis no banco, mas não são necessárias
  como cópias adicionais das vendas no modelo atual.
- Inteiros para códigos/quantidades, datas para calendário e datas de fatos,
  decimais fixos para valores financeiros. IDs e taxas não somam automaticamente.
- Taxas como margem_percentual são frações (0,6027 = 60,27%). Já as taxas
  do forecast são pontos percentuais (7,66 = 7,66%); não aplicar um formato
  que multiplique esse segundo valor por 100.
- Não há medidas nem relacionamentos definidos nos arquivos atuais.
- O forecast é mensal e total da empresa; precisa de tratamento de datas
  na tarefa de modelagem. Não relacioná-lo diretamente por produto/canal/região.

Testes locais já realizados: colunas comparadas com SQL/CSV, referências
das sete tabelas, tipos declarados, JSONs e totais financeiros de referência.
Não foi executado um analisador TMDL ou o motor M nesses testes. A validação
final de abertura, atualização e contagens no Desktop continua pendente.

A conexão pelo Session pooler funcionou: a usuária apresentou o Navegador
com os objetos do banco. Dados de conexão devem ser consultados no painel
Connect do projeto, sem registrar senhas neste documento.

Houve erro de certificado remoto inválido. Foi baixado o certificado
`prod-ca-2021` diretamente do Supabase, identificado como Supabase Root
2021 CA, válido de 28/04/2021 a 26/04/2031. A usuária seguiu a instalação
em Autoridades de Certificação Raiz Confiáveis para o usuário atual;
posteriormente, a conexão apresentou a lista de objetos. Não desativar
SSL como solução automática para erros futuros.

Também apareceu um erro .NET de `StorPSCTL.exe`, da pasta Acer, durante
consulta de informações de energia do computador. Esse relatório não
era do Power BI nem evidência de senha incorreta. Não ativar depuração JIT
ou editar configurações do Windows por causa daquele aviso genérico.

O `.gitignore` exclui `**/.pbi/cache.abf` e `**/.pbi/localSettings.json`.
O cache local foi preservado no computador e não enviado ao GitHub.
Outros arquivos de definição, como editorSettings.json, permanecem versionados.

## 9. Histórico recente e pendências locais

| Commit | Conteúdo |
|---|---|
| `9b4999f` | Análises comerciais e crescimento mensal/anual |
| `6dd8847` | Forecast e comparação com orçamento |
| `6ac9b69` | Validação histórica do forecast |
| `1787d29` | View do forecast para Power BI |
| `1cd9f68` | Projeto Power BI com importações e guia de conexão |

Na conferência de 13/10/2026, antes de criar este documento, a branch main
estava alinhada com a referência local origin/main. Isso reflete o estado
conhecido pelo Git local; conferir novamente ao retomar.

`sql/05_consultas_analiticas.sql` continua sinalizado como modificado,
embora consultas anteriores com `git diff` não tenham mostrado mudança
de conteúdo. Não descartar, restaurar ou incluir automaticamente essa
pendência em commits de outras tarefas. Investigar se necessário.

Um arquivo com nome acidental, começando com “t de receita e comparação”,
foi criado durante uso do visualizador do Git. Seu conteúdo era uma cópia
do diff; foi conferido e apagado com autorização. Não faz parte do projeto.

Pontos de documentação para uma tarefa futura:

- `docs/planejamento.md` ainda apresenta orçamento apenas de setembro a
  dezembro de 2026; o período efetivo é janeiro de 2024 a dezembro de 2026.
- `docs/dicionario_dados.md` ainda não descreve margem_percentual de fato_vendas.
- O dicionário menciona fato_forecast como tabela futura, mas o forecast
  atual é uma consulta/view, sem tabela física própria.
- O README ainda precisa explicar execução, arquitetura, resultados e imagens.

## 10. Etapas futuras, após confirmar a carga

Esta lista é um roteiro, não autorização para executar tudo de uma vez:

1. Modelar e validar relacionamentos e calendário no Power BI.
2. Criar medidas financeiras e comparar com as referências de Python/SQL.
3. Construir páginas: Visão Executiva, Produtos e Marcas, Canais e Regiões,
   Budget x Actual e Forecast.
4. Desenvolver análises complementares no Excel.
5. Atualizar documentação, incluir imagens e preparar apresentação do portfólio.
6. Fazer revisão final de resultados, arquivos e publicação.

## 11. Como usar este arquivo em uma nova conversa

Texto que a usuária pode enviar:

> Leia docs/continuidade_projeto.md e confira o estado atual do repositório.
> Continue do ponto registrado, sem refazer etapas concluídas. Trabalhe
> em uma tarefa por vez, explique em português simples e valide resultados.
> Use somente comandos Git de consulta; eu farei add, commit e push.
> Oriente os registros pela interface Source Control do VS Code e sugira
> mensagens de commit em inglês, mantendo as explicações em português.

Ao concluir cada etapa, atualizar este documento na tarefa autorizada
ou propor sua atualização, registrando o que foi comprovado, o que ainda
está pendente e o único próximo passo.
