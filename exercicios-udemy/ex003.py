import copy
from dados import produtos_dados as dados


novos_produtos = copy.deepcopy(dados.produtos)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in novos_produtos
]

print(novos_produtos)

produtos_ordenados_por_nome = copy.deepcopy(dados.produtos)

produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda item: item['nome'])

print(produtos_ordenados_por_nome)

produtos_ordenados_por_preco = sorted(copy.deepcopy(dados.produtos), key=lambda item: item['preco'])

print(produtos_ordenados_por_preco)
