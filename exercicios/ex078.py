num = list()
maior_valor = 0
menor_valor = 0
pos_maior_v = list()
pos_menor_v = list()

for i in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {i}: '))
    num.append(n)
    maior_valor = max(num)
    menor_valor = min(num)

for i, nu in enumerate(num):
    if nu == maior_valor:
        pos_maior_v.append(i)
    if nu == menor_valor:
        pos_menor_v.append(i)

print('=-'*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior_valor} nas posições', end=' ')
for v in pos_maior_v:
    print(f'{v}.. ', end=' ')
print(f'\nO menor valor digitado foi {menor_valor} nas posições', end=' ')
for v in pos_menor_v:
    print(f'{v}.. ', end=' ')
