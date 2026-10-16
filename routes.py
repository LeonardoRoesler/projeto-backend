#importação da biblioteca
from fastapi import APIRouter

#criação do router 
router = APIRouter(prefix="/tarefas", tags=["tarefas"])

#criação da rota para criar uma tarefa
@router.post("/criar")
async def criar_tarefa():
    ...
    return {"mensagem": "Tarefa criada com sucesso!"}

#criação da rota para listar as tarefas
@router.get("/listar")
async def listar_tarefas():
    ...
    return {"mensagem": "Lista de tarefas!"}
