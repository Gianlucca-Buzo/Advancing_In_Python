from src.main.nota_fiscal import Nota_fiscal
from src.main.criador_de_nota_fiscal import Criador_de_nota_fiscal
from src.main.orcamento import Item
from datetime import date
from pytest import fixture,raises

@fixture
def razao_social():
    return "FHSA Limitada"

@fixture
def cnpj():
    return "012345678910"

@fixture
def itens():
    return [Item("Capinha de Celular", 30.0), Item("Pano de limpeza", 15.0), Item("Carregador USB", 55.0)]

@fixture
def detalhes():
    return "detalhes da nota"

def test_builder_values(razao_social,cnpj,itens,detalhes):
    data_agora = date.today()
    nota_fiscal = (Criador_de_nota_fiscal()
                   .com_razao_social(razao_social)
                   .com_cnpj(cnpj)
                   .com_itens(itens)
                   .build())

    assert nota_fiscal.razao_social == razao_social and nota_fiscal.cnpj == cnpj and nota_fiscal.detalhes == '' and nota_fiscal.data_de_emissao == data_agora
