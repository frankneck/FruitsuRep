from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from .models import Post


def index(request):
    return render(request, 'main_app/base.html')


def auth(request):
    return render(request, 'main_app/auth.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def registration(request):
    return render(request, 'main_app/registration.html')

def UserProfile(request):
    return render(request, 'main_app/UserProfile.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})



