n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

numeros = (n1, n2, n3, n4)
pos_num_3 = numeros.index(3)
qtd_num_9 = numeros.count(9)

print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {qtd_num_9} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {pos_num_3 +1}° posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')
print(f'Os valores pares digitados foram:', end=' ')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
