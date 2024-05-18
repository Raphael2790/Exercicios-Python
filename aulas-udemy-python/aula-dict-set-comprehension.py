produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    # tranformação do dado
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    # filtro de valores
    if chave != 'categoria'
}

dados = [('nome', 'Raphael')]

dados_transformados = {
    chave: valor
    for chave, valor
    in dados
}

s1 = {i ** 2 for i in range(10)}

print(dc, s1, dados_transformados)
