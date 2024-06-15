from functools import partial, reduce
from types import GeneratorType

numeros = (i for i in range(10))
print(isinstance(numeros, GeneratorType))


def aumenta_porcentagem(valor, porcentagem):
    return round(valor * porcentagem)


aumenta_dez_porcento = partial(
    aumenta_porcentagem,
    porcentagem=1.1
)

total = aumenta_dez_porcento(10)

print(total)

# devolve um map object que pode ser iteravel
# um iteravel é esgotavel ou seja só permite a iteração uma vez
# para armazenar os valores é necessário tranformar em listas por exemplo
novos_numeros = map(
    lambda x: x * 3,
    numeros
)

print(list(novos_numeros))
# na segunda tentativa de criar uma lista não existe mais elementos
print(list(novos_numeros))

numeros = [i for i in range(100)]
# devolve um objeto do tipo filter map que é um iteravel
numeros_pares = filter(
    lambda n: n % 2 == 0,
    numeros
)
numeros_pares = list(numeros_pares)

soma = reduce(
    lambda ac, n: ac + n,
    numeros_pares
)

print(soma)
