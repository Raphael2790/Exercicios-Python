def mostra_argumentos(*args, **kwargs):
    print('Não nomeados', args)
    print('Nomeados', kwargs)


pessoa = {
    'nome': 'Raphael',
    'sobrenome': 'Santos'
}
dados_pessoa = {
    'idade': 18,
    'altura': 1.7
}

# retorna apenas as chaves
nome, sobrenome = pessoa
print(nome, sobrenome)

# retorna valores
nome, sobrenome = pessoa.values()
print(nome, sobrenome)

# retorna ambos
(nomeKey, nome), (sobrenomeKey, sobrenome) = pessoa.items()

print(nome, sobrenome)

# Cria um novo dicionário desempacotando dados dos dicionários
dados_completos = {**pessoa, **dados_pessoa}

mostra_argumentos(1, 2, 3, **dados_completos)

# retorna o valor da chave caso não exista retorna None
valor = dados_completos.get('nome')
