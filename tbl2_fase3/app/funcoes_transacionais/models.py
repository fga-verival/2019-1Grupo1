from django.db import models

# Create your models here.

class FuncaoTransacional(models.Model):

    functions_types = (
        ('EE', 'EE'),
        ('CE', 'CE'),
        ('SE', 'SE')
    )

    complexity_types = (
        ('baixa', 'baixa'),
        ('media', 'media'),
        ('alta', 'alta')
    )
      
    nome = models.CharField(max_length=150)

    contador = models.CharField(max_length=150)

    tipo_funcao = models.CharField(
        max_length=10,
        choices=functions_types
    )

    complexidade = models.CharField(
        max_length=40,
        choices=complexity_types
    )

    qtd_alr = models.IntegerField()

    qtd_der = models.IntegerField()
    
    pontos_de_funcao = models.IntegerField()

    data_cadastro = models.DateField()
