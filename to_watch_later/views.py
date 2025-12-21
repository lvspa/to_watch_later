from django.shortcuts import render

def index(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/index.html')

def cads(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/cads.html')