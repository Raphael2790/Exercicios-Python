from random import randint
from time import  sleep


def sortear_valores(lista):
    print('Sorteando valores da lista: ', end=' ')
    for i in range(0, 5):
        n = randint(1, 10)
        print(n, end=' ')
        sleep(0.5)
        lista.append(n)
    print('PRONTO!')


def soma_pares(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares da lista {lista}, temos {soma}')


lista_numeros = list()
sortear_valores(lista_numeros)
soma_pares(lista_numeros)
