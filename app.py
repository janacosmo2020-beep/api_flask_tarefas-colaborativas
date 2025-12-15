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

if __name__ == "__main__":
    app.run(debug=True)