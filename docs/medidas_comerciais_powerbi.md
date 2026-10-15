# Medidas de pedidos, unidades e ticket médio

## O que foi criado

Três medidas em fato_vendas, na pasta Indicadores comerciais:

| Medida | Cálculo |
|---|---|
| Pedidos | DISTINCTCOUNT(fato_vendas[id_pedido]) |
| Unidades Vendidas | SUM(fato_vendas[quantidade]) |
| Ticket Médio | DIVIDE([Receita Líquida], [Pedidos]) |

Um pedido pode aparecer em várias linhas porque contém vários produtos.
Contar linhas não equivale a contar pedidos. A medida Pedidos conta cada
código uma vez dentro do filtro. Não somar pedidos por produto para chegar
ao total: um mesmo pedido pode aparecer em mais de um grupo.

O ticket usa a receita e os pedidos do filtro atual. Com um produto
selecionado, representa a receita daquele produto por pedido que o contém;
não é o valor de toda a cesta desses clientes. O total é recalculado,
sem média simples dos tickets de produtos ou meses.

DIVIDE protege a divisão por zero ou por uma contagem vazia. Os meses
sem vendas continuam em branco. A formatação mostra reais com duas casas,
mas não arredonda antecipadamente a medida.

## Validação local

Os CSVs foram lidos para calcular receita com Decimal, unidades inteiras
e conjuntos de pedidos únicos, no total e em três filtros. Também foi
confirmado que não há id_pedido vazio e que os pedidos por produto não
podem ser somados para representar o total.

Sete medidas existem em fato_vendas: as quatro financeiras anteriores
mais estas três. A Consulta 1 salva é idêntica ao teste independente.
O teste financeiro anterior permanece em validar_medidas_financeiras.dax.
O motor DAX não foi executado nesta validação local.

## Próximas ações no Power BI

1. Reabra powerbi/beauty_analytics.pbip; as edições foram feitas com ele fechado.
2. Clique em Atualizar e aguarde terminar.
3. Abra a Exibição de consulta DAX e selecione Consulta 1.
4. Clique em Executar. O teste já está colocado; não precisa substituir texto.
5. Envie as cinco linhas para conferir com as referências abaixo.
6. Depois da conferência, salve com Ctrl + S. Aguardar orientação para
   fechar antes da próxima edição e reabrir para novos testes.

| Cenário | Receita | Pedidos | Unidades | Ticket |
|---|---:|---:|---:|---:|
| Total realizado | 1.975.524,68 | 15.000 | 31.337 | 131,70 |
| Canal 1 | 545.089,65 | 4.206 | 8.753 | 129,60 |
| Produto 1 | 154.776,97 | 1.749 | 2.392 | 88,49 |
| Agosto 2026 | 59.569,39 | 492 | 945 | 121,08 |
| Setembro 2026 sem realizado | Em branco | Em branco | Em branco | Em branco |

A consulta arredonda o ticket para facilitar a comparação, sem mudar
a medida permanente. A ordem de apresentação das linhas é alfabética.

## GitHub e Supabase

Nenhuma ação no Supabase. Não foram alteradas tabelas ou views do banco.
Após validar, salvar o PBIP e preparar no Source Control apenas:

- definition/tables/fato_vendas.tmdl.
- DAXQueries/Consulta 1.dax.
- powerbi/validar_medidas_comerciais.dax.
- docs/medidas_comerciais_powerbi.md.

Revisar eventuais metadados adicionais antes de incluir. A definição
fato_vendas já tinha lineageTags das medidas anteriores, geradas pelo
Desktop; foram preservadas. Não descartar alterações de outras tarefas.
O progresso continua no documento local ignorado.

Mensagem sugerida: `feat: add order, unit and average ticket measures`.
Fazer Commit e depois ... → Push manualmente, após a revisão.
