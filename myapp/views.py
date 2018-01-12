from django.shortcuts import render, redirect

from myapp.models import Vote, Too, quest








def index(request):
    if request.method == 'POST':
        iname = request.POST.get('inputEmail3')
        too = Too(name=iname)
        print(too.id)
        too.save()
        too = Too.objects.get(name=iname)
        print(too.id)
        request.session['too_id'] = too.id
        print(request.session.items())
        context = {'name': iname}
        return redirect('first')
    return render(request, 'aut_in.html')

def conte (a,b):
    too = Too.objects.get(id=a)
    que1 = quest.objects.get(id=b)
    rname = too.name
    txfo = que1.info
    op1 = que1.option1
    op2 = que1.option2
    op3 = que1.option3
    context = {'name': rname, 'info': txfo, 'op1': op1, 'op2': op2, 'op3': op3}
    return context

def first(request):
    too_id = request.session['too_id']
    if not too_id:
        return redirect('index')
    too = Too.objects.get(id=too_id)
    if request.method == 'GET':
        context = conte(too_id,1)
        return render(request, 'homePage.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        if radio == 'option1':
            radio = 4
        elif radio == 'option2':
            radio = 1
        elif radio == 'option3':
            radio = 2
        too.first = radio
        too.save()
        return redirect('second')
    return render(request, 'homePage.html')





def second(request):
    too_id = request.session['too_id']
    if not too_id:
        return redirect('index')
    too = Too.objects.get(id=too_id)
    if request.method == 'GET':
        context = conte(too_id,2)
        return render(request, 'too_page.html', context)
    elif request.method == 'POST':
        radio = request.POST.get('optionsRadios')
        if radio == 'options1':
            radio = 1
        elif radio == 'options2':
            radio = 3
        elif radio == 'options3':
            radio = 5
        too.second = radio
        too.resO = too.first + too.second
        too.save()
        if too.resO >= 5:
            point = 'балов'
        else:
            point = 'бала'
        context = {'all': too.resO, 'points': point, 'name': too.name}
        return render(request, 'res2.html', context)
    return render(request, 'too_page.html')




def results (request):
    too_id = request.session['too_id']
    if not too_id:
        return redirect('index')
    too = Too.objects.get(id=too_id)
    if request.method == 'POST':
        reth = request.POST.get('bt_res')
        one = too.first
        two = too.second
        fname = too.name
        context = {'one': one, 'two': two, 'name': fname}
        return render (request,'res2.html', context)



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
#     too_id = request.session['too_id']
#     if not too_id:
#         return redirect('index')
#     else:
#         return render(request, 'results')
