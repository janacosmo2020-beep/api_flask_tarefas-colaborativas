from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models.tarefa import TarefaModel
from models.projeto import ProjetoModel
from schemas.tarefa import TarefaSchema, TarefaUpdateSchema

tarefa_blp = Blueprint("Tarefas", __name__, description="Tarefas do projeto")

@tarefa_blp.route("/tarefas")
class TarefaList(MethodView):

    @tarefa_blp.response(200, TarefaSchema(many=True))
    def get(self):
        return TarefaModel.query.all()

    @tarefa_blp.arguments(TarefaSchema)
    @tarefa_blp.response(201, TarefaSchema)
    def post(self, data):
        if not ProjetoModel.query.get(data["projeto_id"]):
            abort(404, message="Projeto não encontrado")

        tarefa = TarefaModel(**data)
        db.session.add(tarefa)
        db.session.commit()
        return tarefa