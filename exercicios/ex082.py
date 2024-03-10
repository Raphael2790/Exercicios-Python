impares = list()
pares = list()
numeros = list()

while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break

print('-='*30)
print(f'Lista completa é {numeros}')
print(f'A lista de pare é {pares}')
print(f'A lista de impares é {impares}')
