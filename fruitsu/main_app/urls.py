from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('EmptyPage/', EmptyPage),
    path('Recipe/', Recipe),
    path('ListOfRecipes/', ListOfRecipes),

]