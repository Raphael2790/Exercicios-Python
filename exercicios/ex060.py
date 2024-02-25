from math import factorial

n = int(input('Digite um número para \n calcular seu fatorial: '))
f = factorial(n)

print(f'Fatorial calculado via func foi {f}')

fatorial = 1
print(f'Calculando {n}! = {n}', end=' ')
while n > 1:
    fatorial *= n
    n -= 1
    print(f'x {n} ', end='')
print(f'= {fatorial}')

