from django import forms
from .models import Pessoa

class CadastrarForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade','email']

        
class EditarForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade','email']