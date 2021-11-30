from src.leilao.dominio import Usuario,Leilao,Lance,Avaliador

lucca = Usuario("Lucca")
isa = Usuario("Isa")

lance_lucca = Lance(lucca,1000.0)
lance_isa = Lance(isa,500.0)

leilao = Leilao("Carros")

leilao.lances.append(lance_lucca)
leilao.lances.append(lance_isa)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')