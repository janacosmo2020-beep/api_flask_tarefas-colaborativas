from flask import Flask
from flask_smorest import Api
from db import db

from resources.projeto import projeto_blp
from resources.tarefa import tarefa_blp

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "API de Tarefas Colaborativas"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)
    api.register_blueprint(projeto_blp)
    api.register_blueprint(tarefa_blp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)