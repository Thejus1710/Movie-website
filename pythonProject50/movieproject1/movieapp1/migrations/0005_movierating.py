# Generated by Django 5.0.6 on 2024-05-17 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp1', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
