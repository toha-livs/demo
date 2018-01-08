from django.db.models import Model, IntegerField, TextField


class Too(Model):
    id = IntegerField(unique=True, primary_key=True)
    name = TextField(null=False)
    first = TextField(null=False)
    second = TextField(null=False)