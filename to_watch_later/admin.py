from django.contrib import admin
from to_watch_later.models import User
from to_watch_later.models import Movie
from to_watch_later.models import ListMovies

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(ListMovies)