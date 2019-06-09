from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
        blank=False,
        validators=[MinValueValidator(0)]
    )

    qtd_der = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(1)]
    )

    pontos_de_funcao = models.IntegerField()

    data_cadastro = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.tipo_funcao == "EE":
            if self.qtd_der >= 1 and self.qtd_der <= 4 and self.qtd_alr >= 0 and self.qtd_alr <= 1:
                self.complexidade = "baixa"
                self.pontos_de_funcao = 3
        super(FuncaoTransacional, self).save(*args, **kwargs)

