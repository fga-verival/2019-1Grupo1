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

    nome = models.CharField(
        max_length=150,
        blank=False
    )

    contador = models.CharField(
        max_length=150,
        blank=False
    )

    tipo_funcao = models.CharField(
        max_length=10,
        choices=functions_types,
        blank=False
    )

    complexidade = models.CharField(
        max_length=40,
        choices=complexity_types,
    )

    qtd_alr = models.IntegerField(
        blank=False
    )

    qtd_der = models.IntegerField(
        blank=False
    )

    pontos_de_funcao = models.IntegerField()

    data_cadastro = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome

    def isvalid(self):
        if(self.nome == '' or self.contador == '' or self.tipo_funcao == '' or self.complexidade == '' or self.qtd_alr == '' or self.qtd_der == '' or self.pontos_de_funcao == ''):
            return False
        else:
            return True

