# -*- coding: UTF-8 -*-
def imprime(nota_fiscal):
    print(f'imprimindo nota fiscal {nota_fiscal.__str__()}')

def envia_por_email(nota_fiscal):
    print(f'Enviando por email nota fiscal {nota_fiscal.razao_social}')

def salva_no_banco(nota_fiscal):
    print(f"Salvando no banco nota fiscal {nota_fiscal.__str__()}")

if __name__ == '__main__':

    from nota_fiscal import Nota_fiscal

    nota_fiscal = Nota_fiscal(razao_social="Razao Social",cnpj= "123456878912",itens=[],observadores=[imprime,envia_por_email,salva_no_banco])