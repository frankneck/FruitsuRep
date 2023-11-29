from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader


def index(request):
    return render(request, 'main_app/base.html')


def login(request):
    return render(request, 'main_app/auth.html')


def pageNotFound(requset, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
