from tkinter.font import names

from django.shortcuts import render, redirect

from to_watch_later.forms import CadastroForm
from django.contrib.auth.models import User


def index(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/index.html')

def cads(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/cads.html')

def login(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/login.html')

def home_user(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/home_user.html')




def cadastro(request):
    if request.method=='POST':
        form=CadastroForm(request.POST)ls

        if form.is_valid():

            name=form.cleaned_data['name']
            user_name=form.cleaned_data[' user_name']
            user_email=form.cleaned_data['user_email']
            password=form.cleaned_data['password']

            User.objects.create_user(
            name=name,
            username=user_name,
            email=user_email,
            password=password
         )
            return redirect('home')

        else:
            return render(request, 'cadastro.html', {'form': form})








