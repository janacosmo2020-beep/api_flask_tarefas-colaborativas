from marshmallow import Schema, fields

class PlainProjetoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)

class PlainTarefaSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True)
    descricao = fields.Str()
    status = fields.Str()