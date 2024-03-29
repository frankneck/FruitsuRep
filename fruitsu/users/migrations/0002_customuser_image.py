# Generated by Django 4.2.7 on 2024-02-02 15:41

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/no_image.jpg', max_length=255, upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
