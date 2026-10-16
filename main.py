#importação da bibliotecas
from fastapi import FastAPI
from routes import router

#configuração do FastAPI
app = FastAPI()

#configuração das rotas
app.include_router(router)
