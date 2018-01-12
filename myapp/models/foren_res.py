from django.db.models import Model, IntegerField, TextField, ForeignKey


class for_res(Model):
    quest_id = ForeignKey()