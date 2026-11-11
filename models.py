from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


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