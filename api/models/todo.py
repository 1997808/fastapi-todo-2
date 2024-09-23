from tortoise.models import Model
from tortoise.fields import CharField, IntField, BooleanField


class Todo(Model):
    id = IntField(pk=True)
    task = CharField(max_length=100)
    done = BooleanField(default=False, null=False)
