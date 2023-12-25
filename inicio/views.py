from django.shortcuts import render , redirect
from inicio.forms import CadastrarForm
from inicio.models import Pessoa

def inicio(request):
    pessoas = Pessoa.objects.all()
    return render(request,"inicio.html",{"pessoas":pessoas})

# insert objects on database
def cadastrar(request):
    contexto = {'sucesso': False}
    form = CadastrarForm(request.POST or None)
    if form.is_valid():
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request,"cadastrar.html" ,contexto)


def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,"editar.html",{'pessoa':pessoa})
