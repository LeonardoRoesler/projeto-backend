from fastapi import FastAPI

from database import criar_tabelas
from routes import router

app = FastAPI(title="lista de Tarefas")

criar_tabelas()
app.include_router(router)

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API de Tarefas!"}