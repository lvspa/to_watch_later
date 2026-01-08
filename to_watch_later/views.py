from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.http import JsonResponse
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
        form=CadastroForm(request.POST)
        if form.is_valid():
            return JsonResponse ({
                'success': True,
                'message': 'Usuário criado!',
                'redirect_url': '/home_user/'
            })
    else:
        return JsonResponse({
            'success': False,
            'message': 'Erro ao criar usuário.',
            'redirect_url': '/cads/'
        })

    form = CadastroForm()
    return render(request, 'cads.html', {'form': form})

#def login_user(request):









