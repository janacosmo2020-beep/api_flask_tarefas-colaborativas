from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API de Tarefas Colaborativas"})

tarefas = [
    {
        "id": 1,
        "titulo": "Reunião de planejamento",
        "descricao": "Organizar o cronograma do projeto.",
        "colaboradores": ["João", "Maria"]
    }
]

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas/<int:id>", methods=["GET"])
def buscar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    nova_tarefa = request.get_json()
    nova_tarefa["id"] = tarefas[-1]["id"] + 1
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

{
  "titulo": "Desenvolvimento de API",
  "descricao": "Criar uma API RESTful utilizando Flask",
  "colaboradores": ["Ana", "Carlos"]
}

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa.update(dados)
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

{
  "titulo": "Desenvolvimento da API RESTful",
  "descricao": "Criar endpoints de GET, POST, PUT, DELETE",
  "colaboradores": ["Ana", "Carlos", "João"]
}

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida"})
    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>/colaboradores", methods=["PUT"])
def adicionar_colaborador(id):
    nome_colaborador = request.get_json().get("colaborador")
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["colaboradores"].append(nome_colaborador)
            return jsonify(tarefa)
    return jsonify({"erro": "Tarefa não encontrada"}), 404

{
  "colaborador": "Carlos"
}

if __name__ == "__main__":
    app.run(debug=True)