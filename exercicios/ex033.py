menor_valor = 0
maior_valor = 0

n1 = int(input('Primeiro valor: '))
menor_valor = n1
maior_valor = n1

n2 = int(input('Segundo valor: '))

if n2 > maior_valor:
    maior_valor = n2
elif n2 < menor_valor:
    menor_valor = n2

n3 = int(input('Terceiro valor: '))

if n3 > maior_valor:
    maior_valor = n3
elif n3 < menor_valor:
    menor_valor = n3

print(f'O maior valor digitado foi {maior_valor}')
print(f'O menor valor digitado foi {menor_valor}')
