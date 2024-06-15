from itertools import zip_longest, count

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# uniao de listas
uniao_lista_por_lista_menor = list(zip(l1, l2))
uniao_lista_por_lista_maior = list(zip_longest(l1, l2, fillvalue='Sem valor'))

# count é um iterador infinito
c1 = count(start=8, step=8)
