

class Desconto_por_tres_itens():

    def __init__(self, proximo_desconto):

        self.__proximo_desconto = proximo_desconto

    def calcula(self,orcamento):

        if orcamento.total_itens > 3:
            return orcamento.valor*0.1
        else:
            return self.__proximo_desconto.calcula(orcamento)

class Desconto_por_valor_maior_que_quinhentos_reais():

    def __init__(self, proximo_desconto):
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.valor > 500:
            return orcamento * 0.07
        else:
            return self.__proximo_desconto.calcula(orcamento)

class Sem_desconto():

    def calcula(self,orcamento):
        return 0

class Calculador_de_descontos:

    #Chain of responsability: Cada objeto tem a responsabilidade de chamar o proximo caso
    #não seja sua responsabilidade fazer o calculo
    def calcula(self,orcamento):

        return Desconto_por_tres_itens(
                Desconto_por_valor_maior_que_quinhentos_reais(
                    Sem_desconto())).calcula(orcamento)
