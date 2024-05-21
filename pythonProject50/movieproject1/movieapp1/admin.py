from django.contrib import admin

from .models import User, Movie, MovieRating

# Register your models here.
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(MovieRating)