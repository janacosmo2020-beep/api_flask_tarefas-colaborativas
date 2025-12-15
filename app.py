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

if __name__ == "__main__":
    app.run(debug=True)