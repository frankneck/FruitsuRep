from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name="register"),
    path('login/', custom_login),
    path('login', custom_login),
    path('logout/', LogoutPage),
    path('profile/<username>', profile, name='profile'),
    path('activate/<uidb64>/<token>', activate, name='activate'),

]