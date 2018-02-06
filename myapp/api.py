
import json

from django.db.models import Sum
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from myapp.models import User, quest, Answer


def seccess_get(a):
    questt = quest.objects.get(id=a)
    txt_quest = {'info': questt.info, 'asw1': questt.option1, 'asw2': questt.option2, 'asw3': questt.option3}
    return txt_quest


def seccess_post(request):
    g = request.body
    g = json.loads(g.decode("utf-8"))
    if g['answer'] == 3:
        g['answer'] = 2
    elif g['answer'] == 2:
        g['answer'] = 6
    else:
        g['answer'] = 4
    user = User(name=g['name'])
    user.save()
    user_id = User.objects.filter(name=g['name']).order_by('-id')[0]
    print(user_id.id)
    answerr = Answer(score=g['answer'], page_number=1, user=user_id)
    answerr.save()
    return user_id.id


def seccess_post_light(request, b):
    g = request.body
    g = json.loads(g.decode('utf-8'))
    if g['answer'] == 3:
        g['answer'] = 2
    elif g['answer'] == 2:
        g['answer'] = 6
    else:
        g['answer'] = 4
    user_id = User.objects.get(id=g['user_id'])
    answerr = Answer(score=g['answer'], page_number=b, user=user_id)
    answerr.save()
    return Response({})

def text(b):
    que1 = quest.objects.get(id=b)
    txfo = que1.info
    op1 = que1.option1
    op2 = que1.option2
    op3 = que1.option3
    context = {'info': txfo, 'op1': op1, 'op2': op2, 'op3': op3}
    return context


@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def quest1(request):
    if request.method == 'GET':
        return Response(seccess_get(1))
    elif request.method == 'POST':
        print('good')
        r = seccess_post(request)
        return Response({'id': r})

@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def quest2(request):
    if request.method == 'GET':
        return Response(seccess_get(2))
    elif request.method == 'POST':
        seccess_post_light(request, 2)

@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def quest3(request):
    if request.method == 'GET':
        return Response(seccess_get(3))
    elif request.method == 'POST':
        seccess_post_light(request, 3)

@api_view(['GET', 'POST'])
@renderer_classes((JSONRenderer,))
def quest4(request):
    if request.method == 'GET':
        return Response(seccess_get(4))
    elif request.method == 'POST':
        seccess_post_light(request, 4)




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



 # questt = quest.objects.get(id=1)
    # if request.method == 'GET':
    #     print(questt)
    #     txt_quest = {'info': questt.info, 'asw1': questt.option1, 'asw2': questt.option2, 'asw3': questt.option3}
    #     return Response(txt_quest)
    # elif request.method == 'POST':
    #     g = request.body
    #     g = json.loads(g.decode('utf-8'))
    #     if g['answer'] == 3:
    #         g['answer'] = 2
    #     elif g['answer'] == 2:
    #         g['answer'] = 6
    #     else:
    #         g['answer'] = 4
    #     user = User(name=g['name'])
    #     user.save()
    #     user_id = User.objects.filter(name=g['name']).order_by('-id')[0]
    #     print(user_id.id)
    #     answerr = Answer(score=g['answer'], page_number=1, user=user_id)
    #     answerr.save()
    #     return Response({})
        # answer = Answer(score=radio, page_number=3, user=user)