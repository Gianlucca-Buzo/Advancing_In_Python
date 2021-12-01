# -*- coding: UTF-8 -*-
# orcamento.py
import numpy as np
from abc import ABCMeta, abstractmethod


class ItemError(Exception):
    pass


class Estado_de_um_orcamento():
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class Em_aprovacao(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        if not orcamento.foi_aplicado_desconto_extra():
            orcamento.desconto_extra = orcamento.valor * 0.02
        else:
            raise Exception('O desconto extra ja foi aplicado')

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovação não pode ir para finalizado')


class Aprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        if not orcamento.foi_aplicado_desconto_extra():
            orcamento.desconto_extra = orcamento.valor * 0.05
        else:
            raise Exception('O desconto extra ja foi aplicado')

    def aprova(self, orcamento):
        raise Exception('Orcamento aprovado não pode ir para aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento aprovado não pode ir para reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orcamento reprovado não pode ir para aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento reprovado não pode ir para reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orcamento finalizado não pode ir para aprovado')

    def reprova(self, orcamento):
        raise Exception('Orcamento finalizado não pode ir para reprovado')

    def finaliza(self, orcamento):
        raise Exception('Orcamento finalizado não pode ir para finalizado')


class Orcamento(object):

    def __init__(self, itens):
        self.__itens = itens
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0
        self.__desconto_extra_aplicado = False

    def aprova(self):
        self.estado_atual.aprova(self)

    def foi_aplicado_desconto_extra(self):
        return self.__desconto_extra_aplicado

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
        self.__desconto_extra_aplicado = True

    @property
    def desconto_extra(self):
        return self.__desconto_extra

    @desconto_extra.setter
    def desconto_extra(self, valor):
        self.__desconto_extra = valor

    @property
    def valor(self):
        return self._soma_valores_dos_itens() - self.__desconto_extra

    def _soma_valores_dos_itens(self):
        return sum(item.valor for item in self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    @property
    def total_itens(self):
        return len(self.__itens)

    @property
    def itens(self):
        return self.__itens

    def aplica_desconto(self):
        pass


class Item():

    def __init__(self, nome, valor):
        self.__nome = nome
        if valor > 0:
            self.__valor = valor
        else:
            raise ItemError('O valor do item tem que ser maior que 0')

    @property
    def valor(self):
        return self.__valor
