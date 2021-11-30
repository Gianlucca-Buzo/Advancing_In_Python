from src.leilao.dominio import Usuario,Leilao
from src.leilao.excecoes import LanceInvalido
import pytest

@pytest.fixture
def lucca():
    return Usuario("Lucca",1500.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_quando_o_usuario_propor_um_lance(lucca,leilao):
    lucca.propor(1000.0,leilao)

    assert lucca.carteira == 500

def test_caso_proponha_um_lance_com_valor_maior_que_a_carteira_gerar_erro(lucca,leilao):
    with pytest.raises(LanceInvalido):
        lucca.propor(2000.0, leilao)