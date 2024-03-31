def valida_preco(texto):
    n = input(texto)
    n = n.replace(',', '.')
    if not n.isalpha():
        return float(n)
    else:
        print(f'ERRO: "{n}" é um preço inválido!')
        return 0.0


def leia_dinheiro(texto):
    preco = valida_preco(texto)
    while preco == 0.0:
        preco = valida_preco(texto)
    return preco
