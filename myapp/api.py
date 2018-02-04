import json

from django.db.models import Sum
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpRequest

from myapp.models import User, quest


def text(b):
    que1 = quest.objects.get(id=b)
    txfo = que1.info
    op1 = que1.option1
    op2 = que1.option2
    op3 = que1.option3
    context = {'info': txfo, 'op1': op1, 'op2': op2, 'op3': op3}
    return context

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def results(request):
    ratings = User.objects.values('name').annotate(rating=Sum('answers__score')).order_by('-rating')[:3]
    result = []
    for item in ratings:
        result.append({
            'name': item['name'],
            'rating': item['rating']
        })
    return Response(result)


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def quest1(request):
    questt = quest.objects.get(id=1)
    if request.method == 'GET':
        print(questt)
        txt_quest = {'info': questt.info, 'asw1': questt.option1, 'asw2': questt.option2, 'asw3': questt.option3}
        return Response(txt_quest)
    elif request.method == 'POST':
        g = request.body
        print(g)
        return Response({})




def some_post_view(request):
     return request.body


