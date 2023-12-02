from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader


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



