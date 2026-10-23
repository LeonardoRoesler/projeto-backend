from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select

app = FastAPI()

#classes - Banco conexão

class TarefaCriar(BaseModel):
    titulo: str
    descricao: Optional[str] = None

class TarefaAtualizar(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False
    prioridade: int = 1 


class Tarefa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False
    prioridade: int = 1


engine = create_engine("sqlite:///tarefas.db")
SQLModel.metadata.create_all(engine)

#Visão Api 

@app.get("/")
def raiz():
    return {"mensagem": "ola,"}

@app.post("/tarefas", response_model=Tarefa, status_code=201)
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
    
@app.get("/tarefas", response_model=list[Tarefa])
def listar_tarefas():
    with Session(engine) as session:
        return session.exec(select(Tarefa)).all()

@app.get ("/tarefas/{tarefa_id}", response_model=Tarefa)
def buscar_tarefa(tarefa_id: int):
    with Session(engine) as session: 
        tarefa = session.get(Tarefa, tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        return tarefa

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
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

@app.delete("/tarefas/{tarefa_id}", status_code=204)
def apagar_tarefa(tarefa_id: int):
    with Session(engine) as session:
        tarefa = session.get(Tarefa, tarefa_id)
        if not tarefa:
            raise HTTPException(status_code=404, detail="Tarefa não encontrada")
        session.delete(tarefa)
        session.commit()


