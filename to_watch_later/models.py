from django.db import models


class Movie (models.Model):
    name=models.CharField(max_length=100)
    gen=models.CharField(max_length=100)
    duration=models.IntegerField()
    data_add=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.gen

    def __str__(self):
        return self.duration


class User (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=300)
    password=models.IntegerField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.email





