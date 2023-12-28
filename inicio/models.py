from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100 )
    idade = models.IntegerField(verbose_name="Idade",blank=True, null=True)
    email = models.EmailField(verbose_name="E-mail",max_length=150)
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]
        
    def __str__(self):
        return self.nome
    
        