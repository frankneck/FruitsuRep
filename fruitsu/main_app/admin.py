from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import Post
from django.contrib import admin
from .models import Recipe, Ingredient, Step

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Recipe)
admin.site.register(Post)