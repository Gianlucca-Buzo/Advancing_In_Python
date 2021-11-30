# -*- coding: UTF-8 -*-
class Imposto():

    def calcula(self,orcamento):
        return orcamento.valor*0.05

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06