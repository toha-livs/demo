from django.contrib import admin

from myapp.models import User, Answer
from .models import quest

admin.site.register(quest)
admin.site.register(User)
admin.site.register(Answer)