from django.shortcuts import render , redirect
from .forms import CadastrarForm , EditarForm
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

# edit objects on database
def editar(request,id):
    pessoas = Pessoa.objects.get(id=id)
    form = EditarForm(request.POST or None, instance=pessoas)
    if form.is_valid():
        form.save()
        return redirect("inicio")
    return render(request,"editar.html")
