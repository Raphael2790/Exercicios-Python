# Ajuda com documentação de funções
help(print)
print(print.__doc__)


# função com parametros opcionais
def escreva(texto, separator='~', espaco_extra=2):
    tamanho_texto = len(texto)
    espaco_total = tamanho_texto + espaco_extra
    print(f'{separator}'*espaco_total)
    print(f'{texto:^{espaco_total}}')
    print(f'{separator}'*espaco_total)


# doc string para documentar o metodo
def soma_pares(lista):
    """
    -> Faz uma soma de numeros pares dentro de uma lista recebida
    lista
        Representa a lista de numeros
    return
        Nenhum
    """
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares da lista {lista}, temos {soma}')
    return soma


# Variaveis declaradas no escopo global do arquivo podem ser acessadas dentro de funções
# Já variaveis dentro de funções existem apenas no escopo da função
# Variaveis com mesmo nome interno ou externos a funções possuem diferentes escopos
# Então a mudança de uma não interfere na outra
def teste(b):
    # referencia a variavel global a
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')

help(soma_pares)

