# Generated by Django 5.0.6 on 2024-05-18 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp1', '0007_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
