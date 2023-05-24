from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CadastroForm, LoginForm
from .models import Professor

# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            professor = Professor(nome=form.cleaned_data['nome'], senha=form.cleaned_data['senha'])
            checkProfessor = Professor.objects.filter(nome=professor.nome).exists()
            if not checkProfessor:
                myuser = User.objects.create(username=professor.nome, password=professor.senha)
                myuser.save()
                professor.save()
                return redirect(cadastro_sucess) 
    else:  
        form = CadastroForm()
    return render(request, 'cadastro/cadastro.html',{
        "form": form
    })

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha=form.cleaned_data['senha']
            user = authenticate(username=nome, password=senha)
            if user is not None:
                login(request, user)
                return redirect() 
            else:
                return redirect() 
    else:  
        form = LoginForm()
    return render(request, 'cadastro/login.html',{
        "form": form
    })

def cadastro_sucess(request):
    return render(request, 'cadastro/cadastro_sucess.html')