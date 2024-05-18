def encontra_primeira_duplicidade(listaNumeros):
    set_numeros = set()
    numero_duplicado = -1

    for item in listaNumeros:
        if item in set_numeros:
            numero_duplicado = item
            break

        set_numeros.add(item)
    return numero_duplicado


numeros = [1, 4, 9, 8, 9, 4, 8]
existe_duplicidade = encontra_primeira_duplicidade(numeros)
print(existe_duplicidade)
