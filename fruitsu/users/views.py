from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Успешное подтверждение почты")
        return redirect('../../login')
    else:
        messages.error(request, "Неправильная ссылка активации")
    return redirect('../../login')



def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message = render_to_string("users/activatemail.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, "Подтвердите почту")
    else:
        messages.error(request, "Проверьте, правильно ли вы ввели почтовый адрес")
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            login(request, user)
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)
       # uname=request.POST.get('username')
        #email = request.POST.get('email')
       # pass1 = request.POST.get('password1')
       # pass2 = request.POST.get('password2')
       # if pass1!=pass2:
         #   messages.error(request, "Пароли не совпадают")
          #  return redirect('../register')
    else:
         form = UserRegistrationForm()

    return render(
        request=request,
        template_name= "users/register.html",
        context={"form": form}
    )
           # user = form.save(commit=False)
           # user=User.objects.create_user(uname,email,pass1)
           # user.is_active=False
           # activateEmail(request, user, email)
            #return redirect('../login')

       # print(uname,email,pass1,pass2)
   # return render(request, 'users/register.html')

def LoginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('../UserProfile')
        else:
           #messages.error(request, "Неверный логин или пароль")
           return redirect('../login')
    return render(request, 'users/login.html')



def LogoutPage(request):
    logout(request)
    messages.success(request, "Успешный выход из профиля")
    return redirect('../login')

def UserProfile(request):
    return render(request, 'users/UserProfile.html')