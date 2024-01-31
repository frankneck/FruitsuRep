from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from .models import Post

def index(request):
    return render(request, 'main_app/base.html', {'title': 'Главная страница'})


def auth(request):
    return render(request, 'main_app/auth.html', {'title': 'Войти'})


def pageNotFound(request, exception):
    return render(request, 'main_app/404.html')


def registration(request):
    return render(request, 'main_app/registration.html', {'title': 'Регистрация'})


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def EmptyPage(request):
    return render(request, 'main_app/EmptyPage.html')


def Recipe(request):
    return render(request, 'main_app/Recipe.html', {'title': 'Блюдо'})


def ListOfRecipes(request):
    return render(request, 'main_app/ListOfRecipes.html', {'title': 'Список блюд'})