# -*- coding: UTF-8 -*-
from src.main.impostos import ISS, ICMS, Imposto
from src.main.orcamento import Orcamento


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento: Orcamento, imposto: Imposto):
        valor = imposto.calcula(orcamento)
        print (valor)

if __name__ == '__main__':

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())