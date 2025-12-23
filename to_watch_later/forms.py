from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Seu nome'
        })
    )
