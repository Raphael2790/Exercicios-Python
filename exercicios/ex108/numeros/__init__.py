def metade(number=0):
    return number / 2


def dobro(number=0):
    return number * 2


def aumentar(number=0, porcentagem=0):
    total = number + ((number * porcentagem) / 100)
    return total


def diminuir(number=0, porcentagem=0):
    total = number - (number * porcentagem/100)
    return total
