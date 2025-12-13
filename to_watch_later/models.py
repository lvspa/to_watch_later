from django.db import models
from django.db.models import options

class Movie(models.Model):
    name_movie = models.CharField(max_length=100)
    gen = models.CharField(max_length=100)
    duration = models.IntegerField()
    # poster=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_movie

    def __str__(self):
        return self.gen

    def __int__(self):
        return self.duration

    #def ____(self):
        return self.date_add

class User (models.Model):

    name_user=models.CharField(max_length=100)
    email=models.EmailField(max_length=300)
    password=models.IntegerField()

    def __str__(self):
        return self.name_user

    def __str__(self):
        return self.email

    def __str__(self):
        return self.movies


class ListMovies(models.Model):
    movies= models.ForeignKey(Movie, on_delete=models.CASCADE)
    users= models.ForeignKey(User, on_delete=models.CASCADE)













