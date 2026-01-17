from marshmallow import Schema, fields
from schemas.plain import PlainTarefaSchema

class TarefaSchema(PlainTarefaSchema):
    projeto_id = fields.Int(required=True)

class TarefaUpdateSchema(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    status = fields.Str(required=False)
    projeto_id = fields.Int(required=False)