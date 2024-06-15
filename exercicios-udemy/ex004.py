def soma_listas(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        l1[i]+l2[i] for i in range(intervalo)
    ]


lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]
lista_soma = soma_listas(lista1, lista2)

print(lista_soma)

lista_soma_zip = [x+y for x, y in zip(lista1, lista2)]

print(lista_soma_zip)
