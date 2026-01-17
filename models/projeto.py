from db import db

class ProjetoModel(db.Model):
    __tablename__ = "projetos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    tarefas = db.relationship(
        "TarefaModel",
        back_populates="projeto",
        cascade="all, delete-orphan"
    )
