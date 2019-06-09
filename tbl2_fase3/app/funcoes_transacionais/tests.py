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

class TestCase3(TestCase):

    def setUp(self):
        self.funcao_obj_ee = FuncaoTransacional.objects.create(
            nome = 'placeholder_name',
            contador = 'placeholder_contador',
            tipo_funcao = 'EE',
            qtd_alr=1,
            qtd_der=1
        )

        self.funcao_obj_se = FuncaoTransacional.objects.create(
            nome = 'placeholder_name',
            contador = 'placeholder_contador',
            tipo_funcao = 'SE',
            qtd_alr=1,
            qtd_der=1
        )

        self.funcao_obj_ce = FuncaoTransacional.objects.create(
            nome = 'placeholder_name',
            contador = 'placeholder_contador',
            tipo_funcao = 'CE',
            qtd_alr=1,
            qtd_der=1
        )

    def test_validating_complexity(self):

        self.assertTrue('baixa', self.funcao_obj_ce.complexidade)
        self.assertTrue('baixa', self.funcao_obj_ee.complexidade)
        self.assertTrue('baixa', self.funcao_obj_se.complexidade)

    def test_null_der_value(self):

        with self.assertRaises(TypeError):
            self.funcao_obj_ce = FuncaoTransacional.objects.create(
                nome = 'placeholder_name',
                contador = 'placeholder_contador',
                tipo_funcao = 'CE',
                qtd_alr=1
            )

