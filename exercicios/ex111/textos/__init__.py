def pergunta_preco(texto):
    n = input(texto)
    if n.isdecimal() or n.isnumeric():
        return float(n)
    else:
        print('Não é um número válido')
        return 0.0

