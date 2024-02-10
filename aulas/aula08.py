import random
from math import sqrt, floor, ceil
import emoji

num = int(input('Digite um numero:'))
raiz = sqrt(num)
print(f"A raiz de {num} é igual a {ceil(raiz)}")
print(f"A raiz de {num} é igual a {floor(raiz)}")

random_number = random.random()
print(random_number)
random_number_inteiro = random.randint(1, 10)
print(random_number_inteiro)

print(emoji.emojize("Olá, Mundo :earth_americas:", language='alias'))
