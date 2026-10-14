# Calendário para análises de tempo

## Configuração

- dim_calendario foi marcada como tabela de datas, com data como chave.
- mes_nome é ordenado por mes_numero, para mostrar janeiro antes de fevereiro.
- A opção de datas automáticas foi desativada no modelo, para usar o calendário explícito.
- ano_mes já usa AAAA-MM e ordena corretamente como texto.
- As sete tabelas, nove relações e receitas foram preservadas.

Uma tabela de datas deve ter datas únicas, sem vazios e sem lacunas.
Essa estrutura permite comparar períodos com funções como DATEADD.
Fonte: [Tabelas de datas no Power BI](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-date-tables).

As datas automáticas criam tabelas ocultas por coluna de data. Neste
projeto, usaremos os campos de dim_calendario nos visuais e filtros de tempo.
Fonte: [Datas automáticas](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-auto-date-time).

## Testes locais

Foram conferidas 1.096 datas consecutivas entre 01/01/2024 e 31/12/2026,
36 meses, ausência de datas vazias/duplicadas, o dia 29/02/2024 e a
correspondência única entre nome e número do mês. As receitas de referência
foram recalculadas dos CSVs com Decimal. Os metadados foram inspecionados.
Não foi executado o motor TMDL ou DAX nesta conferência local.

## Conferir no Desktop

1. Abra powerbi/beauty_analytics.pbip e clique em Atualizar.
2. Selecione dim_calendario e confira em Ferramentas de tabela a opção
   Marcar como tabela de datas: a tabela deve estar marcada com a coluna data.
3. Selecione mes_nome e confira em Ferramentas de coluna a classificação
   pela coluna mes_numero.
4. Em Arquivo → Opções e configurações → Opções → Arquivo atual →
   Carregamento de dados, confira se Data/hora automática está desmarcada.
   O nome e a posição dos menus podem variar conforme a versão instalada.
5. Na Exibição de consulta DAX, substitua apenas o texto da consulta pelo
   conteúdo de powerbi/validar_calendario.dax e clique em Executar.
6. Confira os resultados abaixo e envie qualquer diferença antes de continuar.
7. Após o teste passar, salve com Ctrl + S.

Resultados esperados:

| Campo | Valor |
|---|---:|
| Datas | 1.096 |
| Datas distintas | 1.096 |
| Datas vazias | Em branco (BLANK), quando não há datas vazias |
| Primeira data | 01/01/2024 |
| Última data | 31/12/2026 |
| Dias ausentes | 0 |
| Meses | 36 |
| Dia bissexto 2024 | 1 |
| Receita agosto 2026 | 59.569,39 |
| Receita mês anterior | 56.825,11 |
| Receita mesmo mês ano anterior | 59.096,92 |

O teste usa cálculos somente na consulta. Não cria medidas permanentes.
COUNTROWS retorna BLANK quando o filtro não encontra nenhuma linha;
nesse campo, o resultado vazio confirma ausência de datas vazias.
Se DATEADD não retornar os valores esperados, conferir a marcação da tabela
de datas, a coluna data e a relação ativa com fato_vendas antes de avançar.

## Limites e próximos passos

O calendário termina em dezembro de 2026, mas as vendas terminam em agosto.
Orçamento e forecast são mensais e ficam associados ao primeiro dia do mês;
usar ano_mes nas comparações mensais, sem interpretar valores como metas diárias.
As medidas futuras devem respeitar o corte do realizado da simulação.

Não executar SQL no Supabase nesta tarefa. Após a revisão no Desktop,
preparar no Source Control apenas dim_calendario.tmdl, model.tmdl,
powerbi/validar_calendario.dax e este guia. O model.tmdl já tinha metadados
da Exibição de consulta DAX antes desta tarefa; essa alteração foi preservada.
Revisar separadamente outros arquivos que o Desktop modificar ao salvar.

Mensagem sugerida: `feat: configure calendar for time intelligence`.
Fazer Commit e depois ... → Push manualmente. O documento de progresso
continua local e ignorado. Não incluir outras pendências automaticamente.
