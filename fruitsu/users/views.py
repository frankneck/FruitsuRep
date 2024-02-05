from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django import forms
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .forms import UserRegistrationForm, UserUpdateForm, UserLoginForm
from .decorators import user_not_authenticated
from django.contrib.auth.decorators import login_required


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

    return redirect('../../login/')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'<b>{user}</b>,Пожалуйста проверьте свою электронную почту <b>{to_email}</b> чтобы подтвердить регистрацию <b>Note:</b> Проверьте вкладку спам.')
    else:
        messages.error(request, f'Не получилость отправить письмо на {to_email}, проверьте, правильно ли вы указали почту.')


@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('../../login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
        )

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('../../login')

#
def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Привет <b>{user.username}</b>! Успешный вход в профиль")
                return redirect('../')

        else:
            for key, error in list(form.errors.items()):
                messages.error(request, "Неверный логин или пароль")

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )


def LogoutPage(request):
    logout(request)
    messages.success(request, "Успешный выход из профиля")
    return redirect('../login')


def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            messages.success(request, f'{user_form.username}, Ваш профиль обновлен!')

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(
            request=request,
            template_name="users/UserProfile.html",
            context={"form": form}
        )
    return redirect("UserProfile")
