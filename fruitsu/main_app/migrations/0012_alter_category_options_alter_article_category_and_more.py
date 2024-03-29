# Generated by Django 4.2.8 on 2024-02-10 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_category_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.category', verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
