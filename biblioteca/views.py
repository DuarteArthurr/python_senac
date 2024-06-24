from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Usuario, Livro
from .forms import RegistroForm, LivroForm, PreferenciasForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'biblioteca/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid login details.")
    return render(request, 'biblioteca/login.html')

@login_required
def dashboard(request):
    livros = Livro.objects.filter(usuario=request.user)
    preferencias = request.user.preferencias or {}
    cor_fundo = preferencias.get('cor_fundo', '#ffffff')
    return render(request, 'biblioteca/dashboard.html', {'livros': livros, 'cor_fundo': cor_fundo})

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('dashboard')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form})

@login_required
def personalizar(request):
    if request.method == 'POST':
        form = PreferenciasForm(request.POST)
        if form.is_valid():
            preferencias = form.cleaned_data
            request.user.preferencias = preferencias
            request.user.save()
            return redirect('dashboard')
    else:
        form = PreferenciasForm(initial=request.user.preferencias)
    return render(request, 'biblioteca/personalizar.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
