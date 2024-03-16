from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()

print('Valores sorteados: ')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
    print(f'O jogador{i} tirou {jogadores[f'jogador{i}']} no dado.')
    sleep(1)

jogadores_ordenados = sorted(jogadores, key=jogadores.get, reverse=True)
ranking = sorted(jogadores, key=itemgetter(1), reverse=True)

print('-='*40)
print(f'  == RANKING DOS JOGADORES ==')

count = 1

for i in jogadores_ordenados:
    print(f'{count}° lugar: {i} com {jogadores[i]}')
    sleep(1)
    count += 1
