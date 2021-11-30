
class Conta:
    #Init eh o construtor
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo objeto")
        # dois underlines deixa os atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo = "001"

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo,self.__titular))

    def depositar(self,valor):
        self.__saldo += valor

    def sacar(self,valor):
        self.__saldo -= valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self,titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite

    def __metodoPrivado(self):
        self.__limite += self.__limite/2

    def transferir(self,conta,valor):
        print("Transferindo {} da conta do {} para a conta do(a) {}".format(valor,self.__titular,conta2.getTitular()))
        self.sacar(valor)
        conta.depositar(valor)

    def solicitarAumentoLimite(self):
        self.__metodoPrivado()

    @staticmethod
    def get_codigo():
        return "001"

if __name__ == "__main__":
    conta = Conta(123,"Lucca",1000.0,2000.0)
    conta2 = Conta(321,"Isa",500.0,1000.0)
    print(conta.limite)
    print(conta.titular)

    conta.limite = 1000.0
    conta.titular = "Gianlucca"
    print(conta.limite)
    print(conta.titular)
    print(Conta.get_codigo())
