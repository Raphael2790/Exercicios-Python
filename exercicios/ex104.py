def leia_int(texto):
    num = str(input(texto))
    while not num.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        num = str(input(texto))
    return int(num)


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
