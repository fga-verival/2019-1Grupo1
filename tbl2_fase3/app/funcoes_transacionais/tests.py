from django.test import TestCase
from django.test import Client
from funcoes_transacionais.models import FuncaoTransacional

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = FuncaoTransacional.objects.create(nome='eaeeeeeeee', contador='contador', tipo_funcao='EE', complexidade='baixa', qtd_alr=1, qtd_der=1, pontos_de_funcao=2)
        self.assertTrue(form.isvalid())

    # Invalid Form Data
    def test_UserForm_invalid(self):

        with self.assertRaises(Exception):
            form = FuncaoTransacional.objects.create(nome='', contador='', tipo_funcao='', complexidade='', qtd_alr=0, qtd_der=0, pontos_de_funcao=0)
            self.assertFalse(form.isvalid())

