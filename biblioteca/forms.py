from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Livro

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano_publicacao']

class PreferenciasForm(forms.Form):
    cor_fundo = forms.CharField(label='Cor de Fundo', max_length=7)
