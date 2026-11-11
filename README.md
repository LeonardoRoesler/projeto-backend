# Projeto Back-End

API REST de lista de tarefas, feita com FastAPI e SQLModel, usando SQLite como banco de dados.

## Rodando localmente

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/LeonardoRoesler/projeto-backend.git
cd projeto-backend
```

Crie e ative o ambiente virtual:

```bash
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Windows (Prompt de Comando)
.venv\Scripts\activate.bat

# Linux / macOS
source .venv/bin/activate
```

Instale as dependências e suba o servidor:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

A API fica disponível em `http://127.0.0.1:8000` e a documentação interativa em `http://127.0.0.1:8000/docs`.

