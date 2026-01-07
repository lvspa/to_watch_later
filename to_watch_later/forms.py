from curses.ascii import isdigit, isalpha

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password

from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

#conectar o front para enviar os dados

class CadastroForm(forms.ModelForm):
    username = forms.CharField(max_length=150,required=True)
    email=forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput,required=True)
    class Meta:
        model= User
        fields = ['username', 'email','password']

    def clean_username(self):
        username=self.cleaned_data.get('username')

        if not username:
            self.add_error('username','Por favor, insira algum nome de usuário.')

        elif User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():

            self.add_error('username',f'O nome de usuário {username} já está em uso.')

        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValidationError("Digite um endereço de email válido.")
        else:
            print ("Muito bom! ^^")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email


    def clean(self):
        cleaned_data = super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        elements_pass=len(password)

        if not password:
            self.add_error('password','Insira uma senha !')

        elif elements_pass<8:
            self.add_error('password','Sua senha precisa ter 8 ou mais dígitos.')

        elif isdigit(password) or isalpha(password):
            self.add_error('password','Tente misturar letras e números para ficar mais protegido.')

        elif not confirm_password:
            self.add_error('confirm_password','Confirme sua senha !')

        elif password != confirm_password:
            self.add_error('confirm_password', 'As senhas não conferem.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password=make_password(user.password)
        if commit:
            user.save()
        return user




