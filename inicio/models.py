from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="nome")
    idade = models.IntegerField(blank=True)
    email = models.EmailField(max_length=150,verbose_name="email")
    
    class Meta: #Força que o nome da tabela seja "evento" e não "inicio"
        db_table = 'Pessoa'
    
    def __str__(self):
        return "class <Pessoa>"
        