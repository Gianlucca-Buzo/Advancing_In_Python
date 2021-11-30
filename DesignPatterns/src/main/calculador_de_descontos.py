

class Calculador_de_descontos:

    def calcula(self,orcamento):

        if orcamento.total_itens > 3:
            return orcamento.valor * 0.1
        elif orcamento.valor > 500:
            return orcamento.valor * 0.07