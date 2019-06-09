from django.test import TestCase
from funcoes_transacionais.models import FuncaoTransacional
from django.core.exceptions import ValidationError


import unittest

class TestStringMethods(unittest.TestCase):

    def test_alr_lower_than_one(self):
        funcao = FuncaoTransacional(
                nome="bla",
                contador="42",
                tipo_funcao="CE",
                complexidade="baixa",
                qtd_alr=-1,
                qtd_der=1,
                pontos_de_funcao=42)
        with self.assertRaises(ValidationError):
            funcao.full_clean()

    def test_der_lower_than_one(self):
        funcao = FuncaoTransacional(
                nome="bla",
                contador="42",
                tipo_funcao="CE",
                complexidade="baixa",
                qtd_alr=1,
                qtd_der=0,
                pontos_de_funcao=42)
        with self.assertRaises(ValidationError):
            funcao.full_clean()

    def test_ee_type(self):
        funcao = FuncaoTransacional(
                nome="bla",
                contador="42",
                tipo_funcao="EE",
                complexidade="baixa",
                qtd_alr=1,
                qtd_der=2
                )
        funcao.save()
        self.assertEqual(funcao.pontos_de_funcao, 3)
        self.assertEqual(funcao.complexidade, "baixa")

