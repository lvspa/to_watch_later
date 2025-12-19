from django.shortcuts import render
import os

# Create your views here.

def index(request):
    #path_ext=os.path.abspath('/PycharmProjects/DjangoProject/ToWatchLater/to_watch_later/templates/to_watch_later/index.html')
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/index.html')