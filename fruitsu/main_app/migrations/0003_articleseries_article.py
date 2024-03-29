# Generated by Django 4.2.7 on 2024-02-03 14:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default Name', max_length=255)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('slug', models.SlugField(unique=True, verbose_name='Series slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default Name', max_length=255)),
                ('article_slug', models.SlugField(unique=True, verbose_name='Article slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения')),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main_app.articleseries', verbose_name='Series')),
            ],
        ),
    ]
