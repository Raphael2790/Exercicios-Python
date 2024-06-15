variaveis_globais = globals()


def contador():
    x = 1
    y = 2
    # captura internas ao escopo
    variaveis_locais = locals()
    return x + y


def concatenar(string_inicial=''):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        # nonlocal indica para o python que a variavel está no escopo acima
        # para permitir mudanças no valor real da variavel
        # logo valor final guarda o estado a cada execução da função interna
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
b = c('b')
d = c('d')

print(d)
