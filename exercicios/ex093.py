jogador = dict()

jogador['nome'] = str(input('Nome do jogador: '))
jogador['gols'] = list()
jogador['total_gols'] = 0
qtd_partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for p in range(0, qtd_partidas):
    gols = int(input(f'Quantos gols na partida {p+1}? '))
    jogador['gols'].append(gols)
    jogador['total_gols'] += gols

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador['nome']} jogou {qtd_partidas} partidas.')
for i, p in enumerate(jogador['gols']):
    print(f'=> Na partida {i+1}, fez {p} gols.')
print(f'Foi um total  de {jogador['total_gols']} gols.')
