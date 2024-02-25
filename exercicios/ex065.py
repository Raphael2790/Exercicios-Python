resp = 'S'
count = 0
soma = 0
maior = 0
menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    count += 1
    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    resp = str(input('Quer continuar? [S/N]'))

print(f'Você digitou {count} e a média foi {soma/count:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
