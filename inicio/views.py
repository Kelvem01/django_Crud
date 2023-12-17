from django.shortcuts import render , redirect
from inicio.models import Pessoa

def inicio(request):
    pessoas = Pessoa.objects.all()
    return render(request,"inicio.html",{"pessoas":pessoas})

## inserir pessoas no banco de dados 
def salvar(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    email = request.POST.get('email')
    
    Pessoa.objects.create(
        nome = nome,
        idade = idade,
        email = email
        
    )
    return redirect('/') ## retorna para o banco de dados 