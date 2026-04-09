# CI-CD-Projeto_C214

Sistema de gerenciamento de alunos desenvolvido para a disciplina C14 – Engenharia de Software (Inatel).

## Pré-requisitos

- Python 3.10 ou superior
- pip

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Rode o sistema

```bash
python src/api.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

## 🐳 Rodando com Docker

### Pré-requisitos
- [Docker](https://www.docker.com/products/docker-desktop) instalado

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/Gpatinho/CI-CD-Projeto_C214.git
cd CI-CD-Projeto_C214
```

2. Build da imagem:
```bash
docker build -t sistema-faculdade .
```

3. Rode o container:
```bash
docker run -p 5000:5000 sistema-faculdade
```

4. Acesse no navegador:
```
http://localhost:5000
```


