pessoa = list()
pessoas = list()
maior = menor = 0
menores_pesos = list()
maiores_pesos = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
        menores_pesos.append(pessoa[0])
        maiores_pesos.append(pessoa[0])
    else:
        if pessoa[1] >= maior:
            if pessoa[1] == maior:
                print('Peso maior igual')
                maiores_pesos.append(pessoa[0])
            else:
                print('Peso maior')
                maiores_pesos.clear()
                maiores_pesos.append(pessoa[0])
            maior = pessoa[1]
        if pessoa[1] <= menor:
            if pessoa[1] == menor:
                print('Peso menor igual')
                menores_pesos.append(pessoa[0])
            else:
                print('Peso menor')
                menores_pesos.clear()
                menores_pesos.append(pessoa[0])
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.2f}kg. Peso de', end=' ')
for nome in maiores_pesos:
    print(nome, end=' ')
print(f'\nO menor peso foi de {menor:.2f}kg. Peso de', end=' ')
for nome in menores_pesos:
    print(nome, end=' ')
