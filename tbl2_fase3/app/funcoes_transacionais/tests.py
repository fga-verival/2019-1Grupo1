from django.test import TestCase
from django.test import Client
from funcoes_transacionais.models import FuncaoTransacional
from funcoes_transacionais.views import FTransacionalList

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

    def test_validation_complexity(self):

        self.assertTrue('baixa', self.funcao_obj_ce.complexidade)
        self.assertTrue('baixa', self.funcao_obj_ee.complexidade)
        self.assertTrue('baixa', self.funcao_obj_se.complexidade)
    
    def test_validation_function_points(self):
        self.assertEqual(3, self.funcao_obj_ce.pontos_de_funcao)
        self.assertEqual(3, self.funcao_obj_ee.pontos_de_funcao)
        self.assertEqual(4, self.funcao_obj_se.pontos_de_funcao)

    def test_null_der_value(self):

        with self.assertRaises(TypeError):
            self.funcao_obj_ce = FuncaoTransacional.objects.create(
                nome = 'placeholder_name',
                contador = 'placeholder_contador',
                tipo_funcao = 'CE',
                qtd_alr=1
            )

class TestCase5(TestCase):

    def test_database_inserting(self):

        funcao_obj_ee = FuncaoTransacional.objects.create(
            nome = 'placeholder_name',
            contador = 'placeholder_contador',
            tipo_funcao = 'EE',
            qtd_alr=1,
            qtd_der=1
        )

        query_list = FuncaoTransacional.objects.all()
        self.assertEqual(len(FuncaoTransacional.objects.all()), 1)
        self.assertEqual(query_list[0].nome, 'placeholder_name')
        self.assertEqual(query_list[0].contador, 'placeholder_contador')
        self.assertEqual(query_list[0].tipo_funcao, 'EE')
        self.assertEqual(query_list[0].qtd_alr, 1)
        self.assertEqual(query_list[0].qtd_der, 1)

    def test_database_connection(self):
         funcao_obj_ee = FuncaoTransacional.objects.create(
                    nome = 'placeholder_name',
                    contador = 'placeholder_contador',
                    tipo_funcao = 'EE',
                    qtd_alr=1,
                    qtd_der=1
        )
