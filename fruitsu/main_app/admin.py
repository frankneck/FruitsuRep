from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import Post, ArticleSeries, Article
from django.contrib import admin
from .models import Recipe, Ingredient, Step

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'article_slug', 'series']}),
        ("Content", {"fields": ['content', 'notes']}),
        ("Date", {"fields": ['published', 'modified']})
    ]



admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Recipe)
admin.site.register(Post)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)


