from fastapi.testclient import TestClient
from main import app

# Cliente que vai simular as requisições sem subir o servidor
client = TestClient(app)

# Testa se a resposta da rota raiz ("/") devolve 200 e a mensagem de boas-vindas
def test_raiz():
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert resposta.json() == {"mensagem": "Bem-vindo à API de Tarefas!"}

# Testa se criar uma tarefa devolve 201 e os dados enviados
def test_criar_tarefa():
    resposta = client.post("/tarefas", json={"titulo": "Teste", "descricao": "Descrição do Teste"})
    dados = resposta.json()
    assert resposta.status_code == 201
    assert dados["titulo"] == "Teste"
    assert dados["concluida"] is False
    client.delete(f"/tarefas/{dados['id']}")

# Testa se buscar uma tarefa pelo id devolve 200 e os dados dela
def test_buscar_tarefa():
    tarefa_criada = client.post("/tarefas", json={"titulo": "Teste", "descricao": "Descrição do Teste"})
    dados = tarefa_criada.json()
    id_tarefa = dados["id"]
    resposta = client.get(f"/tarefas/{id_tarefa}")
    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Teste"
    assert resposta.json()["descricao"] == "Descrição do Teste"
    client.delete(f"/tarefas/{id_tarefa}")

# Testa se buscar uma tarefa que não exista retorna 404 e a mensagem de erro
def test_buscar_tarefa_inexistente():
    resposta = client.get("/tarefas/99999")
    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Tarefa não encontrada"

# Testa se listar as tarefas retorna 200 e a lista de tarefas
def test_listar_tarefas():
    tarefa_criada = client.post("/tarefas", json={"titulo": "Teste", "descricao": "Descrição do Teste"})
    dados = tarefa_criada.json()
    id_tarefa = dados["id"]
    resposta = client.get("/tarefas")
    assert resposta.status_code == 200
    ids = [tarefa["id"] for tarefa in resposta.json()]
    assert id_tarefa in ids
    client.delete(f"/tarefas/{id_tarefa}")