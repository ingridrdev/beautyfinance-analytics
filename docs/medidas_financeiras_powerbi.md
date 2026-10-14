# Primeiras medidas financeiras

## Medidas criadas

As quatro medidas estão em fato_vendas, na pasta Indicadores financeiros.
Uma medida calcula o resultado considerando os filtros do relatório;
ela não acrescenta linhas nem modifica as vendas no banco.

| Medida | Regra |
|---|---|
| Receita Líquida | Soma de fato_vendas[receita_liquida] |
| Custo Total | Soma de fato_vendas[custo_total] |
| Margem Bruta | Receita Líquida menos Custo Total |
| Margem Percentual | Margem Bruta dividida por Receita Líquida |

A margem bruta não é lucro líquido: outras despesas não estão nessa base.
A margem percentual usa os totais, sem calcular média simples dos percentuais
das vendas. A medida armazena uma fração e a formatação 0.00% exibe o percentual.
DIVIDE retorna vazio quando a receita é zero ou vazia, evitando divisão
inválida. Fonte: [DIVIDE no DAX](https://learn.microsoft.com/en-us/dax/divide-function-dax).

Os valores em reais têm formato R$ com duas casas decimais. As medidas
respeitam o período filtrado; o total sem filtros inclui todo o realizado
de janeiro de 2024 a agosto de 2026. Elas não incluem forecast ou orçamento.

## Validação local

Cada linha de vendas foi conferida: receita menos custo coincide com a
margem armazenada. Os totais foram recalculados com Decimal para toda a
base, canal 1 e agosto de 2026. As medidas e referências foram inspecionadas;
a consulta salva é idêntica ao arquivo independente de teste.

Não foi executado o motor DAX localmente. A validação final depende da
execução no Power BI Desktop e da conferência abaixo.

## Executar no Power BI

1. Reabra powerbi/beauty_analytics.pbip. As edições foram feitas com o
   aplicativo fechado, conforme combinado.
2. Clique em Atualizar e aguarde terminar.
3. Abra a Exibição de consulta DAX e selecione Consulta 1.
4. O texto já foi substituído pelo teste: não é preciso copiar código.
5. Clique em Executar e envie as quatro linhas para conferir.
6. Após a conferência, salve com Ctrl + S. Feche o aplicativo antes da
   próxima tarefa que editar os arquivos do modelo; reabra quando orientado.

A consulta também está em powerbi/validar_medidas_financeiras.dax.
Não cria medidas temporárias: ela testa as quatro medidas permanentes.

Resultados esperados:

| Cenário | Receita líquida | Custo total | Margem bruta | Margem % |
|---|---:|---:|---:|---:|
| Total realizado | 1.975.524,68 | 784.832,92 | 1.190.691,76 | 60,27 |
| Canal 1 | 545.089,65 | 218.937,34 | 326.152,31 | 59,83 |
| Agosto 2026 | 59.569,39 | 24.968,26 | 34.601,13 | 58,09 |
| Setembro 2026 sem realizado | Em branco | Em branco | Em branco | Em branco |

A consulta multiplica a fração da margem por 100 e arredonda somente para
apresentar a referência. A medida permanente não multiplica por 100 e não
arredonda antecipadamente seus cálculos. A ordem das linhas é alfabética.
Os meses sem realizado não são convertidos automaticamente em vendas zero.

## Registrar após a revisão

Nenhum SQL novo precisa ser executado no Supabase.
No Source Control, revise e prepare pelo + somente os arquivos desta tarefa:

- definition/tables/fato_vendas.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_medidas_financeiras.dax.
- docs/medidas_financeiras_powerbi.md.

Revise separadamente os metadados que o Desktop alterar ao salvar.
Não incluir pendências anteriores do .gitignore, do diagrama ou caches.
O documento de progresso permanece local e ignorado.

Mensagem sugerida: `feat: add core financial measures`.
Faça Commit e depois ... → Push manualmente. Aguardar a revisão antes
de começar outro grupo de medidas ou construir visuais.
