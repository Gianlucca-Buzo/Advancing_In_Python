from pytest import raises,fixture
from src.main.orcamento import ItemError,Item,Orcamento
from src.main.calculador_de_descontos import Calculador_de_descontos


@fixture
def itens():
    return [Item("Celular",1000.0),Item("Tablet",1500.0),Item("Tenis",230.0)]

@fixture
def calculador_de_descontos():
    return Calculador_de_descontos()


def test_caso_valor_do_item_seja_menor_que_zero_gerar_erro():
    with raises(ItemError):
        Item("Celular",-10.0)

def test_valor_do_orcamento_deve_ser_igual_a_soma_dos_valores_dos_itens(itens):
    orcamento = Orcamento(itens)
    assert orcamento.valor == 2730.0

def test_caso_adicione_item_lista_de_itens_deve_ter_mais_um_item(itens):
    orcamento = Orcamento(itens)
    item = Item("Colar",270.0)
    tamanho_anterior = orcamento.total_itens
    orcamento.adiciona_item(item)
    tamanho_desejado = tamanho_anterior + 1
    assert tamanho_desejado == orcamento.total_itens

def test_caso_orcamento_tiver_mais_de_3_itens_aplicar_10_por_cento_de_desconto(itens,calculador_de_descontos):
    orcamento = Orcamento(itens)
    item = Item("Colar", 270.0)
    orcamento.adiciona_item(item)
    valor_com_desconto = calculador_de_descontos.calcula(orcamento)
    valor_desejado = 300.0
    assert valor_desejado == valor_com_desconto