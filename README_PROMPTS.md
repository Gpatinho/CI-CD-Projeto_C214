IA usda:
 - claude code: Sonnet 4.6 e opus 4.6

- Prompt usado para criar o frontend:
Use HTML, CSS e JavaScript puro ou Bootstrap 5 (preferencial). 

Fundo da página: cinza claro (#f5f6f8)
Conteúdo centralizado horizontalmente
Um container principal (card):
Fundo branco
Bordas arredondadas
Sombra leve (box-shadow suave)
Padding interno
Margem superior

Criar uma barra superior com:

Fundo azul (#1565c0)
Texto branco
Padding

Conteúdo alinhado à esquerda:

Título: "INATEL"
Fonte grande
Negrito
Subtítulo abaixo:
"Instituto Nacional de Telecomunicações"
Fonte menor
Opacidade levemente reduzida

Logo abaixo do header, dentro do container:

Texto: "Cadastro de Alunos"
Cor: azul (#1565c0)
Fonte grande (h4)
Negrito
Espaçamento inferior

Linha horizontal com 3 elementos:

BOTÃO "Cadastrar Aluno"
Cor de fundo: verde (#2e7d32)
Texto branco
Ícone de adicionar usuário à esquerda
Bordas arredondadas
Padding
Hover: verde mais escuro
INPUT DE BUSCA
Placeholder: "Buscar aluno pelo nome..."
Largura média (responsivo)
Fundo: cinza claro (#f1f3f4)
Sem borda forte
Bordas arredondadas
Padding interno confortável
BOTÃO DE BUSCA
Ícone de lupa
Fundo branco
Borda azul (#1565c0)
Bordas arredondadas
Mesmo height do input
Hover: fundo azul bem claro

Alinhamento:

Todos na mesma linha
Espaçamento entre elesde 10px
Pode usar flexbox

Criar uma tabela com as seguintes colunas:

Matrícula
Nome
Curso
Período
E-mail
Fundo azul (#1565c0)
Texto branco
Negrito
Padding interno
Bordas arredondadas no topo

Estilo das linhas:

Fundo branco
Linha separadora (#e0e0e0)
Hover opcional com leve destaque
Ícone de lixeira á direita da coluna email
Cor vermelha (#d32f2f)
Centralizado na célula
Cursor pointer
Hover mais escuro

Texto abaixo da tabela:

"Exibindo 0 de 0 aluno(s)"

Cor cinza escuro
Fonte pequena
Margem superior leve

Implementar:

Fidelidade visual alta
HTML semântico
CSS organizado
JavaScript separado
Pode usar Bootstrap + Bootstrap Icons

- prompt usado para ajustar o popup:

Na tela pop-up de cadastrar aluno, o campo Curso deve ser um dropdown com as opções:
Engenharia de Computação;
Engenharia de Software;
Engenharia Elétrica;
Engenharia Biomédia;
Engenharia de Controle e Automação;
Engenharia de Telecomunicações;
Engenharia de Produção;

E o campo de periodo um outro dropdown com as opções de 1º a 10º;

Estilo do dropdown:
Animação de entrada e saída (usando keyframes);

- prompt usado para gerar o arquivo de notificação:

Estou fazendo um projeto de engenharia de software com pipeline CI/CD no GitHub Actions. O projeto é uma API Flask de cadastro de alunos de faculdade com banco SQLite.

Preciso de um script Python que envie um e-mail de notificação ao final do pipeline, informando o resultado da execução.

O script deve:

Ler as credenciais de e-mail (remetente, senha, destinatário) a partir de variáveis de ambiente (EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO), armazenadas como Secrets no GitHub Actions. Se alguma delas estiver faltando, deve imprimir uma mensagem de erro clara;

Ler também variáveis de ambiente do GitHub Actions para montar o corpo do e-mail: status dos testes (TESTS_STATUS), status do build (BUILD_STATUS), status do deploy (DEPLOY_STATUS), nome do repositório (GITHUB_REPOSITORY), número da execução (GITHUB_RUN_NUMBER), ID da execução (GITHUB_RUN_ID) e nome da branch (GITHUB_REF_NAME).

Determinar o status geral do pipeline como "SUCESSO" se tanto os testes quanto o build forem "success", e "FALHA" caso contrário.

Montar o assunto do e-mail no formato: [CI/CD] SUCESSO — repositorio #numero e o corpo com as informações do repositório, branch, número da execução, e os status de testes, build e deploy formatados em maiúsculo.