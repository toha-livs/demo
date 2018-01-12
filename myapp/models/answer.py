from django.db.models import Model, IntegerField, ForeignKey, CASCADE


class Answer(Model):
    id = IntegerField(unique=True, primary_key=True)
    score = IntegerField(null=True)
    user = ForeignKey('User', on_delete=CASCADE, related_name='answers')
    page_number = IntegerField(null=True)
