numeros = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}o. valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
print('-='*30)
