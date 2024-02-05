from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader
from .models import Post, Article, ArticleSeries
from django.conf import settings


def index(request):
    matching_series = ArticleSeries.objects.all()

    return render(
        request=request,
        template_name='main_app/base.html',
        context={"objects": matching_series}
    )


def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()

    return render(
        request=request,
        template_name="main_app/base.html",
        context={"objects": matching_series}
    )


def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(
        request=request,
        template_name='main_app/article.html',
        context={"object": matching_article}
    )


def pageNotFound(request, exception):
    return render(request, 'main_app/404.html')


def EmptyPage(request):
    return render(request, 'main_app/EmptyPage.html')


def Recipe(request):
    return render(request, 'main_app/Recipe.html', {'title': 'Блюдо'})


def ListOfRecipes(request):
    return render(request, 'main_app/ListOfRecipes.html', {'title': 'Список блюд'})
