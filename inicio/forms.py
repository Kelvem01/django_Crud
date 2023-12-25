from django import forms

class CadastrarForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    idade = forms.IntegerField(label='Idade')
    email = forms.EmailField(label='E-mail')
    