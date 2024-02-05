from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register),
    path('login/', LoginPage),
    path('logout/', LogoutPage),
    path('profile/<username>', profile, name='profile'),
    path('activate/<uidb64>/<token>', activate, name='activate'),

]