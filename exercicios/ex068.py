from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)
vitorias = 0

while True:
    numero_computador = randint(0, 10)
    numero_jogador = int(input('Diga um valor: '))
    escolha_jogador = ' '
    while escolha_jogador not in 'PpIi':
        escolha_jogador = str(input('Par ou Ímpar? [P/I]'))
    total = numero_computador + numero_jogador
    resultado = 'PAR' if total % 2 == 0 else 'IMPAR'
    print(f'-' * 20)
    print(f'Você jogou {numero_jogador} e o computador {numero_computador}.Total de {total} DEU {resultado}')
    print('-' * 20)
    if resultado[0].lower() != escolha_jogador.lower():
        print('Você PERDEU!')
        print('-=' * 20)
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        break
    vitorias += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    print('-=' * 20)

