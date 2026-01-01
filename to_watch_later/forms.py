from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class CadastroForm(forms.Form):
    username = forms.CharField(max_length=150)
    email=forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email=self.cleaned_data.get('email').lower()
        try:
            validate_email(email)
        except ValidationError as e:
            raise ValidationError("Não conhecemos o dominio de email usado, consegue usar outro? :).")
        else:
            print("Muito bom! ^^")

        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso.")
        return email


    def clean(self):
        cleaned_data = super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if not password:
            self.add_error('password','Insira uma senha !')

        elif not confirm_password:
            self.add_error('confirm_password','Confirme sua senha !')

        elif password != confirm_password:
            self.add_error('confirm_password', 'As senhas não conferem.')
        return cleaned_data


    def save(self,commit=True):
        user=super.save(commit=False)
        user.g
        user.save()
        return user




