from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index),
    path('Recipe/', Recipe),
    path('ListOfRecipes/', ListOfRecipes),
    path("<series>", views.series, name="series"),
    path("<series>/<article>", views.article, name="article"),
]