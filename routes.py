from fastapi import APIRouter, HTTPException
from sqlmodel import SQLModel, Session, select

from database import engine
from models import Tarefa, TarefaCriar, TarefaAtualizar


router = APIRouter()

# Rotas para Api

@router.post("/tarefas", response_model=Tarefa, status_code=201)
def criar_tarefa(dados: TarefaCriar):
    tarefa = Tarefa(
        titulo=dados.titulo,
        descricao=dados.descricao,
    )
    with Session(engine) as session:
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
        return tarefa
    
@router.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas():
    with Session(engine) as session:
        return session.exec(select(Tarefa)).all()

@router.get ("/tarefas/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int):
    with Session(engine) as session: 
        tarefa = session.get(Tarefa, tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa

@router.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, dados: TarefaAtualizar):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        tarefa.titulo = dados.titulo
        tarefa.descricao = dados.descricao
        tarefa.concluida = dados.concluida
        tarefa.prioridade = dados.prioridade
        session.add(tarefa)
        session.commit()
        session.refresh(tarefa)
        return tarefa

@router.delete("/tarefas/{tarefa_id}", status_code=204)
def apagar_tarefa(tarefa_id: int):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        session.delete(tarefa)
        session.commit()