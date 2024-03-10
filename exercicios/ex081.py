numeros = list()
resp = ''

while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break

print(f'Você digitou {len(numeros)} elementos')
print(f'Os valores em ordem decrscente são: {numeros.sort(reverse=True)}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
    