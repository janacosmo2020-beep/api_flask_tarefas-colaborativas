from flask_smorest import Blueprint, abort
from flask.views import MethodView
import uuid

from db import tarefas
from schemas.tarefa_schema import TarefaSchema, TarefaSchemaUpdate

tarefa_blp = Blueprint(
    "Tarefas",
    __name__,
    description="Operações relacionadas a tarefas colaborativas"
)

@tarefa_blp.route("/tarefas")
class Tarefas(MethodView):

    @tarefa_blp.response(200, TarefaSchema(many=True))
    def get(self):
        return tarefas.values()

    @tarefa_blp.arguments(TarefaSchema)
    @tarefa_blp.response(201, TarefaSchema)
    def post(self, dados):
        tarefa_id = uuid.uuid4().hex
        nova_tarefa = {**dados, "id": tarefa_id}
        tarefas[tarefa_id] = nova_tarefa
        return nova_tarefa


@tarefa_blp.route("/tarefas/<string:tarefa_id>")
class TarefaId(MethodView):

    @tarefa_blp.response(200, TarefaSchema)
    def get(self, tarefa_id):
        if tarefa_id not in tarefas:
            abort(404, message="Tarefa não encontrada")
        return tarefas[tarefa_id]

    @tarefa_blp.arguments(TarefaSchema)
    @tarefa_blp.response(200, TarefaSchema)
    def put(self, dados, tarefa_id):
        if tarefa_id not in tarefas:
            abort(404, message="Tarefa não encontrada")

        if "id" in dados and dados["id"] != tarefa_id:
            abort(400, message="Não é permitido alterar o id")

        tarefas[tarefa_id].update(dados)
        return tarefas[tarefa_id]

    @tarefa_blp.arguments(TarefaSchemaUpdate)
    @tarefa_blp.response(200, TarefaSchema)
    def patch(self, dados, tarefa_id):
        if tarefa_id not in tarefas:
            abort(404, message="Tarefa não encontrada")

        tarefas[tarefa_id].update(dados)
        return tarefas[tarefa_id]

    @tarefa_blp.response(200)
    def delete(self, tarefa_id):
        if tarefa_id not in tarefas:
            abort(404, message="Tarefa não encontrada")

        tarefas.pop(tarefa_id)