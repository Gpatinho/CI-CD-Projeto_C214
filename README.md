# 🎓 Sistema de Gerenciamento de Alunos — Inatel C214

![CI](https://github.com/Gpatinho/CI-CD-Projeto_C214/actions/workflows/ci.yml/badge.svg)

Sistema web para cadastro e gerenciamento de alunos, desenvolvido na disciplina **C214 – Engenharia de Software** do Inatel.

---

## 📋 Sobre o Projeto

O sistema permite cadastrar, listar, editar e remover alunos de uma faculdade. Possui uma interface web moderna e uma API REST completa com banco de dados SQLite. O projeto conta com um pipeline CI/CD automatizado via GitHub Actions com testes, build, deploy e notificação por e-mail.

---

## 🧱 Arquitetura
CI-CD-Projeto_C214/
├── src/
│   ├── api.py                  # API REST com Flask
│   ├── database.py             # Banco de dados SQLite com SQLAlchemy
│   └── sistema_faculdade.py    # Lógica de negócio
├── frontend/
│   ├── index.html              # Interface web
│   ├── css/style.css           # Estilos
│   └── js/app.js               # Consumo da API
├── tests/
│   ├── test_fluxo_normal.py    # 10 testes — fluxo normal
│   └── test_fluxo_extensao.py  # 10 testes — casos de erro
├── .github/workflows/
│   └── ci.yml                  # Pipeline CI/CD
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── README_BACKEND.md
└── README_PROMPTS.md

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python 3.11 | Linguagem principal |
| Flask | Framework web e API REST |
| SQLAlchemy | ORM para banco de dados |
| SQLite | Banco de dados local |
| Bootstrap 5 | Interface web |
| pytest | Testes automatizados |
| Docker | Containerização |
| GitHub Actions | Pipeline CI/CD |

---

## ⚙️ Funcionalidades

- ✅ Cadastrar aluno com nome, e-mail e curso
- ✅ Listar todos os alunos cadastrados
- ✅ Editar nome e e-mail por matrícula
- ✅ Remover aluno por matrícula
- ✅ Matrícula gerada automaticamente e de forma única
- ✅ Busca de alunos por nome

---

## 🚀 Como Rodar

### Sem Docker

**Pré-requisitos:** Python 3.10 ou superior

```bash
# Clone o repositório
git clone https://github.com/Gpatinho/CI-CD-Projeto_C214.git
cd CI-CD-Projeto_C214

# Instale as dependências
pip install -r requirements.txt

# Rode o sistema
python src/api.py
```

Acesse: [http://localhost:5000](http://localhost:5000)

---

### Com Docker 🐳

**Pré-requisitos:** [Docker](https://www.docker.com/products/docker-desktop) instalado

```bash
# Clone o repositório
git clone https://github.com/Gpatinho/CI-CD-Projeto_C214.git
cd CI-CD-Projeto_C214

# Build da imagem
docker build -t sistema-faculdade .

# Rode o container
docker run -p 5000:5000 sistema-faculdade
```

Acesse: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Testes

O projeto possui **20 testes automatizados**:

| Arquivo | Testes | Descrição |
|---------|--------|-----------|
| `test_fluxo_normal.py` | 10 | Fluxo normal do sistema |
| `test_fluxo_extensao.py` | 10 | Casos de erro e extensão |

Para rodar os testes localmente:

```bash
pytest tests/ -v
```

Para gerar relatório HTML:

```bash
pytest tests/ -v --html=report.html --self-contained-html
```

---

## 🔄 Pipeline CI/CD

O pipeline é executado automaticamente a cada push ou pull request na branch `main`.

| Job | Depende de | Descrição |
|-----|------------|-----------|
| `tests` | — | Roda os 20 testes e gera relatório HTML |
| `build` | — (paralelo) | Gera o pacote `.whl` distribuível |
| `deploy` | tests + build | Build e push da imagem Docker no GHCR |
| `notify` | tests + build + deploy | Envia e-mail com status do pipeline |

---

## 📚 Documentação

- [Backend — Endpoints e Banco de Dados](README_BACKEND.md)
- [Prompts de IA utilizados](README_PROMPTS.md)

---

## 👥 Equipe

Desenvolvido por 4 integrantes como parte da disciplina **C214 — Engenharia de Software**
