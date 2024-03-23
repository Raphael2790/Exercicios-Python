def fatorial(numero, show=False):
    resultado = 1
    frase = ''
    for i in range(1, numero+1, 1):
        resultado *= i
        if show:
            frase += f'{i}'
        if i == numero:
            frase += ' = '
        else:
            frase += ' x '
    return f'{frase}{resultado}'


print(fatorial(5, True))
