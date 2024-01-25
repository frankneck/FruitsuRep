from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings


class Ingredient(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    quantity = models.PositiveIntegerField(default=0)


class Category(MPTTModel):
    name = models.CharField(max_length=255, default="Default Name")
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Step(models.Model):
    number_of_step = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    image_of_step = models.ImageField(upload_to='image_of_step/', blank=True)


class Anime(models.Model):
    title = models.CharField(max_length=255, default="Default Name")
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название рецепта', default="Default Name")
    difficult = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Сложность', default=1)
    ingredients = models.ManyToManyField(Ingredient, related_name='used_in_recipes', verbose_name='Ингредиенты')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Рейтинг', default=1)
    anime_title = models.ForeignKey(
        Anime,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Принадлежность к аниме'
    )
    category = models.ForeignKey(
        Category,
        related_name='recipes',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория рецепта'
    )
    time = models.PositiveIntegerField(default=0, verbose_name='Время приготовления')
    photo = models.ImageField(upload_to="recipe_photos/", blank=True, verbose_name='Изображение')
    direction = models.ManyToManyField(Step, verbose_name='Рецепт')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return f"{self.user.username}'s Favorites"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.title

