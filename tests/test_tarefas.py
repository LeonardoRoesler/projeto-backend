from fastapi.testclient import TestClient
from main import app

# Cliente que simula requisições sem subir o servidor
client = TestClient(app)

# Testa se a resposta da rota raiz ("/") devolve 200 e a mensagem de boas vindas
def test_raiz():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Bem-vindo à API de Tarefas!"}

# Testa se criar uma tarefa devolve 201 e os dados enviados.
def test_criar_tarefa():
    resposta = client.post("/tarefas", json={"titulo": "Teste", "descricao": "Descrição do Teste"})
    dados = resposta.json()
    assert resposta.status_code == 201
    assert dados["titulo"] == "Teste"
    assert dados["concluida"] is False
    client.delete(f"/tarefas/{dados['id']}")