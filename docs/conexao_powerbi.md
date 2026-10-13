# Conexão do Power BI com o Supabase

## Objetivo desta etapa

Conectar o Power BI Desktop e importar os dados existentes. Relacionamentos,
medidas e páginas do dashboard serão tratados depois.

## Se o Power BI Desktop ainda não estiver instalado

Abra a Microsoft Store no Windows, procure **Microsoft Power BI Desktop**
da Microsoft e escolha instalar. Depois abra o aplicativo.
A instalação deve ser feita manualmente; nenhum instalador foi executado
na preparação deste guia.

Fonte: [Instalação oficial do Power BI Desktop](https://learn.microsoft.com/pt-br/power-bi/fundamentals/desktop-get-the-desktop).

## Preparação no Supabase

1. Abra o projeto e clique em **Connect**.
2. Selecione **Session pooler** e consulte os parâmetros separados.
3. Use o host, a porta, o banco e o usuário exatamente como aparecem ali.

O Supabase recomenda o pooler em modo de sessão para ferramentas de BI.
Ele permite conexão por IPv4. O usuário do pooler pode incluir a referência
do projeto; não substitua pelo usuário da conexão direta.

Digite a senha do banco somente na janela de autenticação. Ela não é a
senha de login do site nem uma chave da API. Não cole credenciais neste
guia, no código, no terminal ou no GitHub.

Fonte: [Conexões PostgreSQL do Supabase](https://supabase.com/docs/guides/database/connecting-to-postgres).

## Conexão no Power BI Desktop

1. Abra **Obter dados → Mais → Banco de dados PostgreSQL**.
2. Em **Servidor**, informe o host e a porta do Session pooler no formato
   `HOST:PORTA`, substituindo pelos valores do painel.
3. Em **Banco de dados**, informe o banco mostrado no Supabase.
4. Escolha **Importar** e confirme.
5. Na autenticação **Banco de dados**, informe usuário e senha do banco.
6. No Navegador, marque os objetos listados abaixo e escolha **Transformar dados**.

O conector PostgreSQL já inclui o provedor necessário nas versões atuais
do Power BI Desktop. Não instale drivers adicionais preventivamente.
Mantenha a conexão criptografada. Se aparecer erro de SSL/certificado,
interrompa e consulte a mensagem antes de mudar configurações.

Fonte: [Conector PostgreSQL da Microsoft](https://learn.microsoft.com/en-us/power-query/connectors/postgresql).

## Objetos deste projeto para importar

Selecione no esquema `public`:

| Objeto | Uso | Linhas esperadas |
|---|---|---:|
| dim_produtos | Descrição dos produtos | 15 |
| dim_canais | Descrição dos canais | 5 |
| dim_regioes | Descrição das regiões | 5 |
| dim_calendario | Datas para as análises | 1.096 |
| fato_vendas | Vendas realizadas | 22.734 |
| fato_orcamento | Metas de vendas | 9.828 |
| vw_forecast_receita | Previsão e comparação com metas | 4 |

Esta escolha usa as seis tabelas originais e a view do forecast.
As outras views permanecem disponíveis para consultas SQL; não precisamos
importar cópias das mesmas vendas nesta etapa.

## Conferência antes de construir o dashboard

No Power Query, confira se os sete objetos aparecem, se há prévias de dados
e se não há erros de conexão. A prévia pode mostrar só parte das linhas;
as quantidades da tabela acima serão conferidas após a carga completa.

Confira se as datas são reconhecidas como datas e se valores como
`receita_liquida` aparecem como números. Não faça substituições de ponto
por vírgula nos valores: os dados vêm de colunas numéricas do PostgreSQL.

O forecast tem somente totais mensais da empresa. Ele não pode ser dividido
por produto, canal ou região. Seu corte permanece em agosto de 2026,
mesmo que a data real do computador seja posterior.

Não salve um PBIX no repositório nesta etapa. Primeiro confirme a conexão
e revise o modelo; o arquivo pode conter dados importados e informações
da fonte que precisam ser revisadas antes de publicação.

## Se não conectar

Envie apenas o texto do erro, ocultando informações de acesso. Confira
se o projeto está ativo e se host, porta e usuário pertencem todos ao
mesmo Session pooler. Não altere permissões do banco nem desative SSL
para tentar resolver sem identificar a causa.

## Estado da preparação

A conexão real foi estabelecida no Power BI Desktop. O projeto foi salvo
em `powerbi/beauty_analytics.pbip`.

O modelo inicialmente continha apenas o catálogo do banco (colunas como
Name, Data e Schema). Essa definição foi substituída por sete importações
separadas, usando os objetos listados neste guia. Os arquivos TMDL declaram
as colunas e seus tipos e as consultas M selecionam o objeto correspondente
no esquema public. Valores financeiros usam decimais fixos. IDs e taxas
não são somados automaticamente. Medidas e relacionamentos ficam para
a próxima tarefa.

Foram conferidos localmente: referências do modelo, correspondência de
colunas com SQL/CSV, tipos declarados, arquivos JSON, quantidades dos CSVs
e os totais de receita, custo e margem. Não foi executado um analisador
TMDL nem o motor M nesta conferência. A leitura do banco pelas novas
consultas ainda precisa ser confirmada no Power BI Desktop.

## Aplicar a importação configurada nos arquivos

1. Com o Power BI fechado, abra `powerbi/beauty_analytics.pbip`.
2. Clique em **Página Inicial → Atualizar** e aguarde a carga.
3. Se forem solicitadas credenciais, informe a senha atual do banco
   na autenticação do Power BI, sem gravá-la no projeto.
4. Confira se as sete tabelas aparecem e se a atualização terminou sem
   erros. Se houver erro de definição ou carga, envie o texto antes de
   continuar. A tabela antiga Banco de dados PostgreSQL não deve aparecer.
5. Salve o projeto depois da carga bem-sucedida.

Se a versão instalada mostrar um aviso de alterações externas, revise
e aplique essas alterações. O cache local foi preservado; o Power BI pode
precisar recarregar os dados para corresponder ao novo modelo.

Não execute SQL novo no Supabase. Os objetos de origem já existem.

## Registrar no GitHub após a carga ser conferida

Os comandos abaixo são executados manualmente no terminal da pasta do
projeto. Execute um de cada vez. O arquivo SQL 05 fica fora desta etapa.
O `.gitignore` exclui cache.abf e localSettings.json, que são arquivos locais;
as definições do modelo e do relatório permanecem disponíveis para revisão.

```powershell
git status
```

```powershell
git add .gitignore docs/conexao_powerbi.md powerbi/
```

```powershell
git --no-pager diff --cached --stat
```

Confira se não há cache.abf, localSettings.json ou senhas entre as alterações
preparadas. Depois execute:

```powershell
git commit -m "Configura importação das tabelas no projeto Power BI"
```

```powershell
git push origin main
```
