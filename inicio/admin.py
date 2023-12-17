from django.contrib import admin
from inicio.models import Pessoa

# Register your models here.registrar os modelos (objetos)

class PessoaAdmin(admin.ModelAdmin):
    #Mostra os CAMPOS desejados na rota 'admin/'
    list_display = ('nome', 'idade', 'email')

    #Apresenta um filtro interativo pelos CAMPOS definidos
    list_filter = ('nome', 'idade','email' )
    
admin.site.register(Pessoa,PessoaAdmin) #adicionado por kelvem