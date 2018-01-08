from django.db.models import Model, IntegerField, TextField


class Vote(Model):
    id = IntegerField(unique=True, primary_key=True)
    vote = TextField(null=False)

