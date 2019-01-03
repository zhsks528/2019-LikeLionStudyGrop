from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Hello

#http를 받을 거기 때문에 request 인자를 받아줘야한다.
#GET hello/   

def hello(request):

    
    # ORM => Object Relation Mapping
    post = Hello.objects.all()

    context = {
        'post' : post,
    }

    return render(request, 'hello/index.html', context=context )