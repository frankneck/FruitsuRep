from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Пароли не совпадают")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('../login')

        print(uname,email,pass1,pass2)
    return render(request, 'users/register.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('../UserProfile')
        #else:
           # return HttpResponse("Пароли не совпадают")
    return render(request, 'users/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('../login')

def UserProfile(request):
    return render(request, 'users/UserProfile.html')