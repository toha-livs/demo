from django.db.models import Model, IntegerField, TextField


class User(Model):
    id = IntegerField(unique=True, primary_key=True)
    name = TextField(null=False)
    # answers

    def __str__(self):
        return '<User id={} name={}>'.format(self.id, self.name)
