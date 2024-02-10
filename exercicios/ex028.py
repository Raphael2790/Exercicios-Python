from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
numero_aleatorio = randint(0, 5)
numero_escolhido = int(input('Em que número eu pensei? '))
print('-=-' * 20)
print('PROCESSANDO...')

sleep(2)

if numero_escolhido == numero_aleatorio:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero_aleatorio} e não no {numero_escolhido}!')
