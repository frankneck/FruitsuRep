from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'main_app/main_page.html', {'title': 'Главная страница', 'anime_titles': Anime.objects.all()})


def auth(request):
    return render(request, 'main_app/auth.html', {'title': 'Войти'})


def pageNotFound(request, exception):
    return render(request, 'main_app/404.html')


def registration(request):
    return render(request, 'main_app/registration.html', {'title': 'Регистрация'})


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})


def RecipeF(request):
    return render(request, 'main_app/Recipe.html', {'title': 'Блюдо'})


def ListOfRecipes(request):
    return render(request, 'main_app/ListOfRecipes.html', {'recipes': Recipe.objects.all(), 'title': 'Список блюд'})
