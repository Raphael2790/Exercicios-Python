num = list()
resp = ' '

while resp not in 'nN':
    v = int(input('Digite um valor: '))
    if v not in num:
        num.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N]'))

num.sort()
print(f'Você digitou os valores: {num}')
