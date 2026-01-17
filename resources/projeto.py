from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models.projeto import ProjetoModel
from schemas.projeto import ProjetoSchema

projeto_blp = Blueprint("Projetos", __name__, description="Projetos colaborativos")

@projeto_blp.route("/projetos")
class ProjetoList(MethodView):

    @projeto_blp.response(200, ProjetoSchema(many=True))
    def get(self):
        return ProjetoModel.query.all()

    @projeto_blp.arguments(ProjetoSchema)
    @projeto_blp.response(201, ProjetoSchema)
    def post(self, data):
        projeto = ProjetoModel(**data)
        db.session.add(projeto)
        db.session.commit()
        return projeto