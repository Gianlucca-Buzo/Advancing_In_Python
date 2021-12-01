# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Template_de_impostos_condicional():

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self,orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self,orcamento):
        pass

class Imposto():

    def calcula(self,orcamento):
        return orcamento.valor*0.05


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

class ICPP(Template_de_impostos_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self,orcamento):
        return format(orcamento.valor * 0.07,'.2f')

    def minima_taxacao(self,orcamento):
        return format(orcamento.valor * 0.05,'.2f')

class IKCV(Template_de_impostos_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return format(orcamento.valor * 0.1,'.2f')

    def minima_taxacao(self, orcamento):
        return format(orcamento.valor * 0.06,'.2f')

    def __tem_item_maior_que_100_reais(self,orcamento):

        for item in orcamento.itens:
            if item.valor > 100:
                return True
        return False