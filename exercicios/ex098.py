from time import sleep


def contar(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    passo_utilizado = passo
    if fim < inicio and passo > 0:
        passo_utilizado *= -1
    final = fim + 1 if passo > 0 else fim - 1
    for n in range(inicio, final, passo_utilizado):
        print(f'{n}', end=' ')
        sleep(1)
    print('FIM!')
    print('-='*30)


contar(1, 10, 1)
contar(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = input('Passo: ')

if passo == ' ':
    passo = 1
else:
    passo = int(passo)

contar(inicio, fim, passo)
