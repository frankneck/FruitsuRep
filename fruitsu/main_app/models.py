from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

from django.template.defaultfilters import slugify
import os

class Category(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 160, unique = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"

class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField("Название оняме", max_length=200)
    subtitle = models.CharField("Краткое описание", max_length=200, default="", blank=True)
    slug = models.SlugField("Слаг", null=False, blank=False, unique=True)
    published = models.DateTimeField("Время публикации", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField("Изображение", default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField("Название рецепта", max_length=200)
    subtitle = models.CharField("Краткое описание", max_length=200, default="", blank=True)
    article_slug = models.SlugField("Слаг", null=False, blank=False, unique=True)
    content = HTMLField("Ингредиенты", blank=True, default="")
    notes = HTMLField("Приготовление", blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(
        ArticleSeries, default="", verbose_name="Оняме", on_delete=models.SET_DEFAULT
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True,
    )
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField("Изображение", default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']

