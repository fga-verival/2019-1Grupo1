from django.db import models
import logging

logger = logging.getLogger(__name__)

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

    def save(self, *args, **kwargs):

        

        if(self.tipo_funcao == 'EE'):

            # e a implementacao da tabela
            if(self.qtd_alr >= 0 and self.qtd_alr <= 1):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 5 and self.qtd_der <= 15):
                    complexidade = 'baixa'
                elif(self.qtd_der >=16):
                    complexidade = 'media'
 
            elif(self.qtd_alr == 2):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 5 and self.qtd_der <= 15):
                    complexidade = 'media'
                elif(self.qtd_der >=16):
                    complexidade = 'alta'

            elif(self.qtd_alr>=3):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'media'
                elif(self.qtd_der >= 5 and self.qtd_der <= 15):
                    complexidade = 'alta'
                elif(self.qtd_der >=16):
                    complexidade = 'alta'

        elif(self.tipo_funcao == 'CE'):

            # implementacao das regras na tabela CE
            if(self.qtd_alr >= 0 and self.qtd_alr <= 1):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 5 and self.qtd_der <= 19):
                    complexidade = 'baixa'
                elif(self.qtd_der >=20):
                    complexidade = 'media'
 
            elif(self.qtd_alr>=2 and self.qtd_alr <=3):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 5 and self.qtd_der <= 19):
                    complexidade = 'media'
                elif(self.qtd_der >=20):
                    complexidade = 'alta'

            elif(self.qtd_alr>=4):

                if(self.qtd_der >=1 and self.qtd_der <= 4):
                    complexidade = 'media'
                elif(self.qtd_der >= 5 and self.qtd_der <= 19):
                    complexidade = 'alta'
                elif(self.qtd_der >=20):
                    complexidade = 'alta'


        elif(self.tipo_funcao ==  'SE'):

            # implementacao das regras na tabela SE
            if(self.qtd_alr >= 0 and self.qtd_alr <= 1):

                if(self.qtd_der >=1 and self.qtd_der <= 5):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 6 and self.qtd_der <= 19):
                    complexidade = 'baixa'
                elif(self.qtd_der >=20):
                    complexidade = 'media'
 
            elif(self.qtd_alr>=2 and self.qtd_alr <=3):

                if(self.qtd_der >=1 and self.qtd_der <= 5):
                    complexidade = 'baixa'
                elif(self.qtd_der >= 6 and self.qtd_der <= 19):
                    complexidade = 'media'
                elif(self.qtd_der >=20):
                    complexidade = 'alta'

            elif(self.qtd_alr>=4):

                if(self.qtd_der >=1 and self.qtd_der <= 5):
                    complexidade = 'media'
                elif(self.qtd_der >= 6 and self.qtd_der <= 19):
                    complexidade = 'alta'
                elif(self.qtd_der >=20):
                    complexidade = 'alta'


        else:
            logger.error(self.tipo_funcao)
            raise Exception('Tipo não existente %s' % self.tipo_funcao)
            
        
        super().save(*args, **kwargs)
