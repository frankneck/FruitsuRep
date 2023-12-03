from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
from .models import Post

admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Compound)
admin.site.register(models.Recipe)
admin.site.register(Post)
