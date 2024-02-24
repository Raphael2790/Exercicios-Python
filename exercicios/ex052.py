num = int(input('Digite um número: '))
cont = 0

for n in range(1, num+1):
    if num % n == 0:
        print(f'\033[1;33m{n}\033[m', end=' ')
        cont += 1
    else:
        print(f'\033[1;31m{n}\033[m', end=' ')

print(f'\nO número {num} foi divisivel {cont} vezes')

if cont == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
