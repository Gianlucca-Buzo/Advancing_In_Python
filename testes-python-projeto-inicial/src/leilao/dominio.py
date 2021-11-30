import sys
from src.leilao.excecoes import LanceInvalido



class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.__maior_lance = 0.0
        self.__menor_lance = 0.0

    @property
    def lances(self):
        return self.__lances[:]

    def tem_lances(self):
        return self.__lances

    def usuarios_diferentes(self,lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido('O mesmo usuario nao pode dar dois lances seguidos')

    def valor_maior_que_o_anterior(self,lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        else:
            raise LanceInvalido('O valor do lance deve ser maior que o lance anterior')

    def lance_eh_valido(self,lance):
        return not self.tem_lances() or (self.usuarios_diferentes(lance) and
                                         self.valor_maior_que_o_anterior(lance))

    def addLance(self,lance : Lance):
        if self.lance_eh_valido(lance):
            if not self.tem_lances():
                self.__menor_lance = lance.valor
            self.__lances.append(lance)
            self.__maior_lance = lance.valor

    @property
    def maior_lance(self):
        return self.__maior_lance

    @property
    def menor_lance(self):
        return self.__menor_lance

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def valor_eh_valido(self,valor):
        return valor <= self.__carteira

    def propor(self,valor,leilao : Leilao):
        if self.valor_eh_valido(valor):
            lance = Lance(self.__nome,valor)
            leilao.addLance(lance)
            self.__carteira -= valor
        else:
            raise LanceInvalido('O valor do lance deve ser menor ou igual que o da sua carteira')