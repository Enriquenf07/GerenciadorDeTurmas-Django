from django.shortcuts import render

# Create your views here.

def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def login(request):
    return render(request, 'cadastro/login.html')
