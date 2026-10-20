# Planejamento da página Visão Executiva

Data: 15/10/2026. Estado: plano aprovado pela usuária e primeira versão
implementada. Página e filtros de mês/canal conferidos em 20/10/2026;
ver visao_executiva_powerbi.md para evidências e limites da validação.

## Objetivo

Permitir que uma pessoa entenda rapidamente a receita, o custo, a margem,
o volume de pedidos e o desempenho contra a meta. A página deve responder:
como a empresa está, como evoluiu nos meses e onde a receita se concentra?

O projeto já possui as medidas necessárias para esta proposta. Nenhuma
medida adicional será criada nesta tarefa. O dashboard ainda não foi
construído quando este plano foi escrito. Os elementos abaixo registram
as decisões que orientaram a primeira versão da página.

## Período e filtros

- Estado inicial: ano 2026, com todos os meses realizados disponíveis
  selecionados. Resultado inicial: janeiro a agosto de 2026.
- Limite da página: dim_calendario[data] até 31/08/2026, corte da simulação.
  Não usar a data real do computador como corte do projeto fictício.
- Filtro de ano com seleção única, permitindo 2024, 2025 ou 2026.
- Filtro de meses a partir de dim_calendario[ano_mes], com seleção de meses
  completos. Para 2024 e 2025, todos os meses podem ser consultados.
- Filtros adicionais: marca (dim_produtos), canal (dim_canais) e região
  (dim_regioes), inicialmente sem restrição.
- Ano e meses devem deixar o período selecionado visível ao leitor.
  Ao mudar o ano, conferir se o filtro de meses não reteve meses incompatíveis.
- Usar as dimensões nos filtros. Não usar IDs das tabelas de fatos como segmentadores.

O orçamento comparável acompanha o período e as dimensões selecionados.
As receitas de 2024/2025 são histórico realizado, não previsão. A página
de Forecast será construída separadamente em uma tarefa futura.

## Indicadores principais

Seis cartões na faixa superior. Um cartão é um número em destaque com
nome e unidade claros. Usar as medidas explícitas já validadas:

| Cartão | Medida | Exibição |
|---|---|---|
| Receita líquida | [Receita Líquida] | R$, duas casas |
| Custo total | [Custo Total] | R$, duas casas |
| Margem bruta | [Margem Bruta] | R$, duas casas |
| Margem percentual | [Margem Percentual] | Percentual, duas casas |
| Pedidos | [Pedidos] | Inteiro com separador de milhar |
| Ticket médio | [Ticket Médio] | R$, duas casas |

Inicialmente, manter os valores completos nos cartões para facilitar a
conferência. Evitar arredondar a ponto de esconder diferenças da validação.
Margem bruta não representa lucro líquido. O ticket respeita o recorte
selecionado e pedidos são contados sem repetição.

## Gráficos e comparação com orçamento

| Visual | Eixo/categoria | Valores | Pergunta respondida |
|---|---|---|---|
| Colunas agrupadas por mês | dim_calendario[ano_mes], crescente | [Receita Líquida], [Receita Orçada Comparável] | A receita atingiu a meta de cada mês? |
| Linha de margem percentual | dim_calendario[ano_mes], crescente | [Margem Percentual] | A rentabilidade melhorou ou piorou? |
| Barras horizontais por região | dim_regioes[nome_regiao] | [Receita Líquida], ordem decrescente | Onde a receita está concentrada? |

Ao lado do gráfico de receita versus orçamento, dois cartões menores:

- Variação em reais: [Variação Receita Orçamento].
- Variação percentual: [Variação Receita Orçamento %].

Esses dois indicadores respondem pelo período filtrado. Usar sinal de
positivo/negativo e nomes claros, além de cor. O orçamento no gráfico é
o comparável, para manter o mesmo período das vendas.

Nos detalhes ao passar o mouse sobre um mês, incluir:

- [Unidades Vendidas].
- [Crescimento Receita MoM %].
- [Crescimento Receita YoY %].

As taxas só são definidas para um mês completo. No total de vários meses
ficam vazias; não criar cartões com taxas acumuladas a partir dessas
medidas nem substituir seus vazios por zero.

## Distribuição proposta

Manter o tamanho atual da página, 1920 por 1080, com ajuste à tela.

| Faixa | Conteúdo |
|---|---|
| Cabeçalho | BeautyFinance Analytics — Visão Executiva; indicação de dados fictícios e corte ago/2026 |
| Filtros | Ano, meses, marca, canal e região, com rótulos visíveis |
| Indicadores | Seis cartões principais, alinhados e com tamanhos consistentes |
| Área central | Receita versus orçamento, em área maior; margem percentual, ao lado |
| Área inferior | Receita por região; dois cartões de variação contra orçamento |

Usar margens regulares, espaços entre grupos e poucos elementos decorativos.
Evitar cortar títulos ou depender de rolagem para ler os indicadores.

Direção visual proposta: fundo claro, cartões brancos, títulos em ameixa
escura, receita em ameixa e orçamento em cinza. Positivo em verde e negativo
em vermelho, sempre acompanhados de sinal/texto. Não depender apenas das
cores para comunicar resultado. A aparência será revisada na construção.

## Interações

- Segmentadores filtram todos os visuais da página.
- Selecionar uma região deve filtrar os demais visuais, sem apenas destacar
  uma parte das colunas; conferir as interações durante a construção.
- Selecionar um mês permite conferir seus cartões e detalhes mensais.
- Deve ser possível limpar uma seleção e retornar aos totais do período.
- A página de Forecast não deve herdar automaticamente filtros de
  marca/canal/região, pois a previsão não tem esse detalhamento.
- Não sincronizar filtros entre páginas sem uma decisão e um teste próprios.

## Referências para o estado inicial

Valores recalculados localmente dos CSVs com Decimal, para janeiro a agosto
de 2026, sem filtro de marca, canal ou região:

| Indicador | Esperado |
|---|---:|
| Receita líquida | R$ 497.957,18 |
| Custo total | R$ 206.597,98 |
| Margem bruta | R$ 291.359,20 |
| Margem percentual | 58,51% |
| Pedidos | 3.872 |
| Ticket médio | R$ 128,60 |
| Unidades, nos detalhes | 7.939 |
| Orçamento comparável | R$ 479.918,23 |
| Variação em reais | R$ 18.038,95 |
| Variação percentual | 3,76% |

Esses valores não são os totais de todo o histórico. Os cartões do estado
inicial não devem mostrar a receita de 1.975.524,68, que inclui 2024/2025.
As referências de custo, margem, pedidos e ticket para esse período exato
precisam de conferência no Desktop quando a página for construída.

## Critérios de validação da futura construção

1. Abrir e atualizar o PBIP sem erros, sem alterar as fontes de dados.
2. Conferir os cartões iniciais com a tabela de referência.
3. Conferir agosto/2026: receita 59.569,39, orçamento 57.792,52 e diferença 1.776,87.
4. Testar canal 1 em agosto: receita 15.262,98, MoM 10,36% e YoY -7,66%.
5. Conferir ausência de YoY em 2024 por falta de histórico anterior.
6. Conferir meses em ordem e meses futuros fora desta página de realizado.
7. Conferir que as barras regionais somam a receita do período e que os
   percentuais agregados não são médias simples.
8. Limpar filtros e confirmar retorno ao estado inicial ou ao período escolhido.
9. Conferir nomes, moedas, percentuais e legibilidade na tela inteira.

Os testes da página no Desktop ainda não foram executados. A primeira versão
dos visuais está implementada e passou na validação local de schemas,
referências e geometria, conforme visao_executiva_powerbi.md.

## Próximas ações

A proposta foi aprovada. A próxima ação é reabrir o Power BI, atualizar e
conferir a primeira versão conforme visao_executiva_powerbi.md.
Não é necessário executar SQL no Supabase.

Para registrar apenas o plano: no Source Control, revisar este arquivo,
prepará-lo pelo +, usar `docs: plan executive overview page`, clicar em
Commit e depois ... → Push. Deixar outras pendências separadas.
O documento de progresso continua local e ignorado.

Após a aprovação, próxima tarefa única proposta: construir a página
Visão Executiva conforme este plano, testando filtros e valores. Confirmar
que o Desktop está salvo e fechado antes da edição externa; orientar quando
reabrir, atualizar, validar e salvar. Não construir outras páginas nessa tarefa.
