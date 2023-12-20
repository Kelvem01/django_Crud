from django.shortcuts import render , redirect
from inicio.models import Pessoa

def inicio(request):
    pessoas = Pessoa.objects.all()
    return render(request,"inicio.html",{"pessoas":pessoas})

# insert objects on database
def cadastrar(request):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    email = request.POST.get("email")
    pessoa = Pessoa(nome=nome,idade=idade,email=email)
    pessoa.save()
    return redirect("inicio")


def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,"editar.html",{'pessoa':pessoa})