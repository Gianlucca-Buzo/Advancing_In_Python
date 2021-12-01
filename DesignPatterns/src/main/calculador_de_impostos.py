# -*- coding: UTF-8 -*-
from src.main.impostos import ISS, ICMS, Imposto
from src.main.orcamento import Orcamento

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento: Orcamento, imposto):
        valor = imposto.calcula(orcamento)
        return valor