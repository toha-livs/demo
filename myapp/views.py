from django.db.models import Sum
from django.shortcuts import render, redirect

from myapp.models import Vote, User, quest, Answer


def take_user_info(request):
    user_id = request.session['user_id']
    if not user_id:
        return redirect('index')
    user = User.objects.get(id=user_id)
    return user




def index(request):
    if request.method == 'POST':
        iname = request.POST.get('inputEmail3')
        user = User(name=iname)
        print(user.id)
        user.save()
        user = User.objects.get(name=iname)
        print(user.id)
        request.session['user_id'] = user.id
        print(request.session.items())
        context = {'name': iname}
        return redirect('first')
    return render(request, 'aut_in.html')


def conte(a, b):
    user = User.objects.get(id=a)
    que1 = quest.objects.get(id=b)
    rname = user.name
    txfo = que1.info
    op1 = que1.option1
    op2 = que1.option2
    op3 = que1.option3
    context = {'name': rname, 'info': txfo, 'op1': op1, 'op2': op2, 'op3': op3}
    return context


def first(request):
    user = take_user_info(request)
    if request.method == 'GET':
        context = conte(user.id, 1)
        return render(request, 'homePage.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        print(radio)
        if radio == 'option1':
            radio = 4
        elif radio == 'option2':
            radio = 1
        elif radio == 'option3':
            radio = 2
        answer = Answer(score=radio, page_number=1, user=user)
        answer.save()
        return redirect('second')
    return render(request, 'homePage.html')


def second(request):
    user = take_user_info(request)
    if request.method == 'GET':
        context = conte(user.id, 2)
        return render(request, 'too_page.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        if radio == 'options1':
            radio = 1
        elif radio == 'options2':
            radio = 3
        elif radio == 'options3':
            radio = 5
        answer = Answer(score=radio, page_number=2, user=user)
        answer.save()
        return redirect('third')
    return render(request, 'user_page.html')


def third(request):
    user = take_user_info(request)
    if request.method == 'GET':
        context = conte(user.id, 3)
        return render(request, 'third_page.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        if radio == 'options1':
            radio = 4
        elif radio == 'options2':
            radio = 1
        elif radio == 'options3':
            radio = 2
        print (radio)
        answer = Answer(score=radio, page_number=3, user=user)
        answer.save()
        return redirect('fourth')
    return render(request, 'too_page.html')


def fourth(request):
    user = take_user_info(request)
    if request.method == 'GET':
        context = conte(user.id, 4)
        return render(request, 'fourth_page.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        if radio == 'options1':
            radio = 2
        elif radio == 'options2':
            radio = 6
        elif radio == 'options3':
            radio = 4
        answer = Answer(score=radio, page_number=4, user=user)
        answer.save()
        return redirect('results')
    return render(request, 'too_page.html')


def results(request):
    user = take_user_info(request)
    answers = Answer.objects.filter(user_id=user.id).all()
    print(answers)
    res = 0
    for ans in answers:
        print(ans)
        res += ans.score
    if res >= 5:
        point = 'баллов'
    else:
        point = 'балла'
    # ratings = User.objects.order_by('-rating')[:3]
    ratings = User.objects.values('name').annotate(rating=Sum('answers__score')).order_by('-rating')[:3]
    context = {'all': res, 'points': point, 'name': user.name, 'ratings': ratings}
    return render(request, 'res2.html', context)


def vote(request):
    # select * from myapp_vote
    # pony = Vote.objects.all()

    # select * from myapp_vote where vote='pony'
    # pony = Vote.objects.filter(vote='pony').all()

    # select count(*) from myapp_vote
    # count = Vote.objects.count()

    # select count(*) from myapp_vote where vote='pony'
    # count = Vote.objects.filter(vote='pony').count()

    pony_count = Vote.objects.filter(vote='pony').count()
    homeless_count = Vote.objects.filter(vote='homeless').count()
    lexus_count = Vote.objects.filter(vote='lexus').count()
    context = {'pony_count': pony_count, 'homeless_count': homeless_count, 'lexus_count': lexus_count}
    if request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        vote = Vote(vote=radio)
        vote.save()
        return render(request, 'voteSuccess.html')
    return render(request, 'votePage.html', context)

# def results(request):
#     user_id = request.session['user_id']
#     if not user_id:
#         return redirect('index')
#     else:
#         return render(request, 'results')
