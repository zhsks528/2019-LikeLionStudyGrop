from django.shortcuts import render
from django.http import HttpResponse
from world.models import Post
#http를 받을 거기 때문에 request 인자를 받아줘야한다.
#GET hello/

def world(request):

    post = Post.objects.all()

    context = {
        'post' : post,
    }
    return render(request, 'world/index.html', context=context)