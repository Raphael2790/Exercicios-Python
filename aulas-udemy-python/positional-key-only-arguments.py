# A barra indica que o parametros anteriores só podem ser usado como posicionais
def adicionar(a, b, /):
    return a + b


# * indica que após o mesmo somente deve se usar argumentos nomeados
def subtrair(a, b, *, c, **kwargs):
    return a - b - c - sum([n for _, n in kwargs.items()])
