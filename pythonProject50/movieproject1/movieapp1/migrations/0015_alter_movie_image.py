# Generated by Django 5.0.6 on 2024-05-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp1', '0014_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
