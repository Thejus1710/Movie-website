# Generated by Django 5.0.6 on 2024-05-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp1', '0005_movierating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
