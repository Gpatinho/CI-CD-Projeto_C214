# ⚙️ Documentação do Backend

## Tecnologias
- **Flask** — framework web para a API REST
- **SQLAlchemy** — ORM para comunicação com o banco de dados
- **SQLite** — banco de dados local (`alunos.db`)

---

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `src/api.py` | API REST com Flask — define todas as rotas |
| `src/database.py` | Configuração do banco SQLite com SQLAlchemy |
| `src/sistema_faculdade.py` | Lógica de negócio — CRUD em memória |

---

## 🔗 Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/alunos` | Lista todos os alunos |
| POST | `/api/alunos` | Cadastra um novo aluno |
| PUT | `/api/alunos/<matricula>` | Atualiza nome e e-mail |
| DELETE | `/api/alunos/<matricula>` | Remove um aluno |

---

## 📤 Exemplos de Requisição

### Cadastrar aluno — POST `/api/alunos`
```json
{
  "nome": "João Silva",
  "email": "joao@email.com",
  "curso": "Engenharia de Software"
}
```

### Resposta
```json
{
  "matricula": "5423",
  "nome": "João Silva",
  "email": "joao@email.com",
  "curso": "ENGENHARIA DE SOFTWARE"
}
```

### Atualizar aluno — PUT `/api/alunos/5423`
```json
{
  "nome": "João Souza",
  "email": "joao.souza@email.com"
}
```

### Deletar aluno — DELETE `/api/alunos/5423`


Retorna status 204 (sem conteúdo)

---

## 🗄️ Banco de Dados

O projeto usa **SQLite** com a seguinte estrutura:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| matricula | String (PK) | Número aleatório único gerado automaticamente |
| nome | String | Nome completo do aluno |
| email | String | E-mail do aluno |
| curso | String | Curso em letras maiúsculas |

O arquivo `alunos.db` é criado automaticamente na primeira execução.

---

## 🔄 Fluxo de Funcionamento

Frontend (index.html)
↓
app.js (fetch)
↓
Flask API (api.py)
↓
SistemaFaculdade (sistema_faculdade.py)  ←→  SQLite (database.py)

1. O frontend faz requisições para a API Flask
2. A API processa via `SistemaFaculdade` (lógica em memória)
3. Os dados são persistidos no banco SQLite
4. A API retorna JSON para o frontend

---

## ▶️ Como Rodar o Backend

### Sem Docker
```bash
pip install -r requirements.txt
python src/api.py
```

### Com Docker
```bash
docker build -t sistema-faculdade .
docker run -p 5000:5000 sistema-faculdade
```

Acesse: [http://localhost:5000](http://localhost:5000)