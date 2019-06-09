from django.test import TestCase
from django.test import Client
from funcoes_transacionais.models import FuncaoTransacional

class Setup_Class(TestCase):

    def setUp(self):
        self.testando = FuncaoTransicional.objects.create(nome='nome', contaddor='contador', tipo_funcao='EE', complexidade='baixa', qtd_alr=1, qtd_der=1, pontos_de_funcao=2)

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': "user", 'first_name': "user", 'phone': 12345678})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})
        self.assertFalse(form.is_valid())

