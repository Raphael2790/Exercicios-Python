# List Comprehension permite criar uma lista com uma logica de iterador interna a notação de array
lista = [numero * 2 for numero in range(10)]

produtos = [
    {'nome': 'p1', 'preco': 10},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # condição de transformação do dado
    if produto['preco'] > 10 else {**produto}
    for produto in produtos
    # condição que será usada para filtrar o dado
    if (produto['preco'] >= 20 and produto['preco'] * 1.05 > 10)
]

numeros = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(numeros)

print(novos_produtos)
