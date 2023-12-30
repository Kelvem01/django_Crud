from django.shortcuts import render , redirect
from .forms import CadastrarForm 
from inicio.models import Pessoa

def inicio(request):
    pessoas = Pessoa.objects.all()
    return render(request,"inicio.html",{"pessoas":pessoas})

# insert objects on database
def cadastrar(request):
    contexto = {'sucesso': False}
    form = CadastrarForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request,"cadastrar.html" ,contexto)

# list pessoas on database

def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request,"listar.html",{"pessoas":pessoas})

# edit objects on database
def update(request,id):
    pessoa = Pessoa.objects.get(id=id)
    form = CadastrarForm(request.POST or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request,"update.html",{'form':form})

#show detail object on database
def detalhes(request):
    pessoas = Pessoa.objects.all()
    return render(request,"detalhes.html",{"pessoas":pessoas})

#delete object on database
def delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('listar')