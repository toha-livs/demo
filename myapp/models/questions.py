from django.db.models import Model, IntegerField, TextField



class quest(Model):
    title = TextField(max_length=30)
    info = TextField(null=True)
    option1 = TextField(null=True)
    option2 = TextField(null=True)
    option3 = TextField(null=True)


    def __str__(self):
        return '<title={} info={} option1={} option2={} option3={}>' .format(self.title, self.info, self.option1, self.option2, self.option3)