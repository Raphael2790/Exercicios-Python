from time import sleep
from random import randint

opcoes = ["PEDRA", "PAPEL", "TESOURA"]

esc_comp = randint(0, 2)
print('Suas opções: ')
print(f'[ 0 ] {opcoes[0]}')
print(f'[ 1 ] {opcoes[1]}')
print(f'[ 2 ] {opcoes[2]}')
esc_jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 20)
print(f'Computador jogou {opcoes[esc_comp]}')
print(f'Jogador jogou {opcoes[esc_jog]}')
print('-=' * 20)

if esc_jog == esc_comp:
    print('EMPATE')
elif (esc_jog == 0 and esc_comp == 2) or (esc_jog == 1 and esc_comp == 0) or (esc_jog == 2 and esc_comp == 1):
    print("JOGADOR VENCE")
else:
    print("COMPUTADOR VENCE")
