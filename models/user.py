from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.BigIntField(unique=True)
    full_name = fields.CharField(max_length=255,null=True)
    username = fields.CharField(max_length=255,unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)

