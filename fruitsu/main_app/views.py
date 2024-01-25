from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from .models import Post


def index(request):
    return render(request, 'main_app/base.html')


def auth(request):
    return render(request, 'main_app/auth.html')


def pageNotFound(request, exception):
    return render(request, 'main_app/404.html')


def registration(request):
    return render(request, 'main_app/registration.html')


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def EmptyPage(request):
    return render(request, 'main_app/EmptyPage.html')


def Recipe(request):
    return render(request, 'main_app/Recipe.html')


def ListOfRecipes(request):
    return render(request, 'main_app/ListOfRecipes.html')


def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Python Bytes'})
