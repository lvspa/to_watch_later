from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.http import JsonResponse
from django.shortcuts import render, redirect
from to_watch_later.forms import CadastroForm
from django.contrib.auth.models import User
import json


def index(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/index.html')

def re_cads(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/cadastro/cads.html')

def login(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/login/login.html')

def home_user(request):
    return render(request,'/home/Alexandre/PycharmProjects/DjangoProject/ToWatchLater/templates/home/home_user.html')


def cads(request):
    if request.method=='POST':
        data_body=request.body
        data_encond=data_body.decode(encoding='UTF-8',errors='strict')
        json_to_dic=json.loads(data_encond)
        form=CadastroForm(json_to_dic)
        if form.is_valid():
            return JsonResponse ({
                'success': True,
                'message': 'Usuário criado!',
                'redirect_url': '/home_user/'
            })
        else:
            return JsonResponse({
                'success':False,
                'errors':print(form.errors.get_json_data())
            })

    else:
        form = CadastroForm()
        return render(request, 'cadastro/cads.html', {'form': form})
    


#def login_user(request):









