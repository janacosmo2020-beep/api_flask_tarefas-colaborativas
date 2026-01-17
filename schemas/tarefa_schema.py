from marshmallow import Schema, fields

class TarefaSchema(Schema):
    id = fields.Str(required=False)
    titulo = fields.Str(required=True)
    descricao = fields.Str(required=False)
    responsavel = fields.Str(required=True)
    status = fields.Str(required=True)

class TarefaSchemaUpdate(Schema):
    titulo = fields.Str(required=False)
    descricao = fields.Str(required=False)
    responsavel = fields.Str(required=False)
    status = fields.Str(required=False)