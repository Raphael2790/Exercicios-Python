def leia_int(texto):
    num = str(input(texto))
    while not num.isnumeric():
        print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        num = str(input(texto))
    return int(num)


def leia_float(texto):
    num = str(input(texto))
    while num.isalpha():
        print('\033[0;31mERRO! Digite um número flutuante válido\033[m')
        num = str(input(texto))
    return float(num)
