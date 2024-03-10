numeros = list()

for n in range(0, 6):
    pos = 0
    num = int(input('Digite um valor: '))
    if len(numeros) == 0:
        numeros.append(num)
        print('Adicionado ao final da lista')
    else:
        if numeros[-1] < num:
            numeros.append(num)
            print('Adicionado ao final da lista')
        else:
            for indice in range(0, len(numeros)):
                if numeros[indice] < num < numeros[indice + 1]:
                    pos = indice + 1
            numeros.insert(pos, num)
            print(f'Adicionado na posição {pos} da lista')

print(f'Os valores digitados em ordem são: {numeros}')
