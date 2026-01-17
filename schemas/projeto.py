from marshmallow import fields
from schemas.plain import PlainProjetoSchema, PlainTarefaSchema

class ProjetoSchema(PlainProjetoSchema):
    tarefas = fields.List(
        fields.Nested(PlainTarefaSchema()),
        dump_only=True
    )