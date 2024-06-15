# Define o que será exportado do modulo
# Evitando que quando se use o import * seja disponibilizado tudo interno ao modulo
__all__ = [
    'metade',
    'dobro',
    'aumentar',
    'diminuir'
]


def metade(number):
    return number / 2


def dobro(number):
    return number * 2


def aumentar(number, porcentagem):
    total = number + ((number * porcentagem) / 100)
    return total


def diminuir(number, porcentagem):
    total = number - (number * porcentagem/100)
    return total


x = 'Alguma coisa'
