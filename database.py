from sqlmodel import SQLModel, create_engine 

engine = create_engine("sqlite:///tarefas.db")

def criar_tabelas():
    SQLModel.metadata.create_all(engine)