# Generated by Django 4.2.7 on 2024-02-05 08:43

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_remove_category_parent_remove_favorite_recipes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default/no_image.png', max_length=255, upload_to=main_app.models.Article.image_upload_to),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='image',
            field=models.ImageField(default='default/no_image.png', max_length=255, upload_to=main_app.models.ArticleSeries.image_upload_to),
        ),
    ]
