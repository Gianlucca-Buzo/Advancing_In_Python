# -*- coding: UTF-8 -*-
# orcamento.py
import numpy as np
class ItemError(Exception):
    pass

class Orcamento(object):
  def __init__(self, itens):
    self.__itens = itens

  @property
  def valor(self):
    return self._soma_valores_dos_itens()

  def _soma_valores_dos_itens(self):
    return sum(item.valor for item in self.__itens)

  def adiciona_item(self,item):
    self.__itens.append(item)

  @property
  def total_itens(self):
    return len(self.__itens)

  def aplica_desconto(self):
    pass

class Item():

  def __init__(self,nome,valor):
    self.__nome = nome
    if valor > 0:
      self.__valor = valor
    else:
      raise ItemError('O valor do item tem que ser maior que 0')

  @property
  def valor(self):
    return self.__valor