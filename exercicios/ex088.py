from random import randint
from time import sleep

sorteios = list()
numeros = list()

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
qtd = int(input('Quantos jogos voce quer que eu sorteie? '))

print(f'-=-=-= SORTEANDO {qtd} JOGOS -=-=-=')
for n in range(0, qtd):
    while len(numeros) < 6:
        sorteado = randint(1, 60)
        if sorteado not in numeros:
            numeros.append(sorteado)
    numeros.sort()
    sorteios.append(numeros[:])
    numeros.clear()

for index, jogo in enumerate(sorteios):
    print(f'Jogo {index+1}: {jogo}')
    sleep(1)

print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
