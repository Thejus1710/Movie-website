from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    password=models.CharField(max_length=8)

class Movie(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField()
    trailer=models.URLField()
    actors=models.TextField()
class MovieRating(models.Model):
    rating=models.IntegerField()
    user=models.ForeignKey('User',on_delete=models.CASCADE)
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE)