from django.db.models import Model, IntegerField, TextField



class quest(Model):
    title = TextField(max_length=30)
    info = TextField(null=True)
    option1 = TextField(null=True)
    option2 = TextField(null=True)
    option3 = TextField(null=True)


    def __str__(self):
        return self.title