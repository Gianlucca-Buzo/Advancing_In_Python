from pytest import raises,fixture
from src.main.orcamento import ItemError,Item,Orcamento
from src.main.calculador_de_descontos import Calculador_de_descontos
from src.main.impostos import ISS,ICMS,ICPP,IKCV
from src.main.calculador_de_impostos import Calculador_de_impostos

#Total eh 2730.0
@fixture
def itens():
    return [Item("Celular",1000.0),Item("Tablet",1500.0),Item("Tenis",230.0)]

#Total eh 100.0
@fixture
def itens_baratos():
    return [Item("Capinha de Celular",30.0), Item("Pano de limpeza",15.0), Item("Carregador USB",55.0)]

@fixture
def calculador_de_descontos():
    return Calculador_de_descontos()

@fixture
def calculador_de_impostos():
    return Calculador_de_impostos()


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

def test_caso_orcamento_nao_corresponda_as_regras_de_desconto_deve_retornar_desconto_zero(calculador_de_descontos):
    orcamento = Orcamento([Item("Tenis",230.0)])

    desconto = calculador_de_descontos.calcula(orcamento)

    assert 0 == desconto

def test_caso_orcamento_custar_mais_que_500_reais_calcular_maxima_taxacao_ICPP(itens,calculador_de_impostos):
    orcamento = Orcamento(itens)

    imposto = calculador_de_impostos.realiza_calculo(orcamento,ICPP())

    assert format(191.1,'.2f') == format(imposto,'.2f')

def test_caso_orcamento_custar_menos_ou_igual_a_500_reais_calcular_minima_taxacao_ICPP(itens_baratos,calculador_de_impostos):
    orcamento = Orcamento(itens_baratos)

    imposto = calculador_de_impostos.realiza_calculo(orcamento,ICPP())

    assert format(5.0,'.2f') == format(imposto,'.2f')


def test_caso_orcamento_custar_mais_que_500_reais_e_tiver_um_item_que_vale_mais_de_100_reais_calcular_maxima_taxacao_IKCV(itens,calculador_de_impostos):
    orcamento = Orcamento(itens)

    imposto = calculador_de_impostos.realiza_calculo(orcamento,IKCV())

    assert format(273,'.2f') == format(imposto,'.2f')

def test_caso_orcamento_custar_menos_ou_igual_a_500_reais_ou_nao_tiver_um_item_que_vale_mais_de_100_reais_calcular_minima_taxacao_IKCV_com_ICPP(itens_baratos,calculador_de_impostos):
    orcamento = Orcamento(itens_baratos)

    imposto = calculador_de_impostos.realiza_calculo(orcamento,IKCV(ICPP()))

    assert format(11.0,'.2f') == format(imposto,'.2f')

def test_caso_orcamento_custar_menos_ou_igual_a_500_reais_ou_nao_tiver_um_item_que_vale_mais_de_100_reais_calcular_minima_taxacao_ISS_com_ICMS(itens_baratos,calculador_de_impostos):
    orcamento = Orcamento(itens_baratos)

    imposto = calculador_de_impostos.realiza_calculo(orcamento,ISS(ICMS()))

    assert format(66.0,'.2f') == format(imposto,'.2f')