from unittest import TestCase
from src.leilao.dominio import Usuario,Lance,Leilao
from src.leilao.excecoes import LanceInvalido


class UnityTestLeilao(TestCase):

    def setUp(self):
        self.lucca = Usuario("Lucca",1500.0)
        self.isa = Usuario("Isa",1000.0)
        self.lance_lucca = Lance(self.lucca, 1000.0)
        self.lance_isa = Lance(self.isa, 500.0)
        self.leilao = Leilao("Carros")


    def test_quando_o_usuario_propor_um_lance_e_for_menor_ou_igual_sua_carteira_retornar_o_menor_e_o_maior(self):
        self.isa.propor(500,self.leilao)
        self.lucca.propor(1000,self.leilao)
        menor_valor_esperado = 500
        maior_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_quando_o_usuario_propor_um_lance_e_for_maior_sua_carteira_gerar_excecao(self):
        self.isa.propor(500, self.leilao)
        with self.assertRaises(LanceInvalido):
            self.lucca.propor(2000, self.leilao)
            menor_valor_esperado = 500
            maior_valor_esperado = 1000

            self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_quando_adicionado_um_unico_lance_deve_retornar_o_mesmo_valor_para_maior_e_o_menor_valor(self):
        self.leilao.addLance(self.lance_lucca)
        menor_valor_esperado = 1000

        self.assertEqual(menor_valor_esperado,self.leilao.menor_lance)
        self.assertEqual(self.leilao.menor_lance,self.leilao.maior_lance)


    def test_quando_recebe_varios_lances_sem_ordem_retornar_o_menor_e_o_maior_valor(self):
        enrico = Usuario("Enrico",700.0)
        giovana = Usuario("Giovana",1100.0)

        lance_enrico = Lance(enrico,700.0)
        lance_giovana = Lance(giovana,1100.0)

        self.leilao.addLance(self.lance_isa)
        self.leilao.addLance(lance_enrico)
        self.leilao.addLance(self.lance_lucca)
        self.leilao.addLance(lance_giovana)


        menor_valor_esperado = 500
        maior_valor_esperado = 1100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_caso_o_leilao_nao_tenha_lances_permitir_propor_lance(self):
        self.leilao.addLance(self.lance_lucca)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1,quantidade_de_lances_recebido)

    def test_caso_ultimo_usuario_seja_diferente_permitir_propor_lance(self):
        self.leilao.addLance(self.lance_isa)
        self.leilao.addLance(self.lance_lucca)

        self.assertEqual(2,len(self.leilao.lances))


    def test_caso_ultimo_usuario_seja_igual_nao_permitir_propor_lance(self):
        self.leilao.addLance(self.lance_isa)
        novo_lance_isa = Lance(self.isa,1100.0)
        with self.assertRaises(LanceInvalido):
            self.leilao.addLance(novo_lance_isa)

        self.assertEqual(1, len(self.leilao.lances))

    def test_caso_valor_lance_for_menor_que_o_ultimo_gerar_excessao_e_nao_permitir(self):
        self.leilao.addLance(self.lance_lucca)
        with self.assertRaises(LanceInvalido):
            self.leilao.addLance(self.lance_isa)

