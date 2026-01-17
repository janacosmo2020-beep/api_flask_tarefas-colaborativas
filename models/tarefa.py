from db import db

class TarefaModel(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    status = db.Column(db.String(50), default="pendente")

    projeto_id = db.Column(
        db.Integer,
        db.ForeignKey("projetos.id", ondelete="CASCADE"),
        nullable=False
    )

    projeto = db.relationship("ProjetoModel", back_populates="tarefas")