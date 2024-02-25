from random import randint

numero_computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
c = 0
acertou = False

while not acertou:
    n = int(input('Qual é seu palpite? '))
    c += 1
    if n == numero_computador:
        acertou = True
    else:
        if n > numero_computador:
            print('Menos...Tente mais uma vez.')
        elif n < numero_computador:
            print('Mais...Tente mais uma vez')

print(f'Acertou em {c} tentativas.Parabéns!')
