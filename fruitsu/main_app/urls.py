from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('Recipe/', RecipeF),
    path('ListOfRecipes/', ListOfRecipes),
]