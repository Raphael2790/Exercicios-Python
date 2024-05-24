from sys import getsizeof

# Iteradores e Iteraveis
# Objetos iteraveis possuem seu iterador interno para entrega dos valores
# Podemos criar nosso proprios objetos iteravereis e iteradores
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)
# Ao chamar next mudamos o iteravel salvo interno ao iterador até que não tenha mais valores
# Similar ao padrão de projeto "Iterator"
valor = next(iterator)

# Generators
# principal diferença de listas é que não coloca todos objetos na memoria em tempo de execução
lista = [i for i in range(100000)]
generator = (i for i in range(100000))
alocacao_generator = getsizeof(generator)
alocacao_lista = getsizeof(lista)

for i in generator:
    print(i)

print(alocacao_generator, alocacao_lista)


# Essa funcão tem como retorno um generator pela utilização da palavra yield
# Diferente do dotnet a palavra return só será atingida ao fim da iteracao como controle de fluxo
def generator1(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return 'Acabou'


def generator2(gen=None):
    resultado = 1
    if gen is not None:
        yield from gen()
    # executa mais alguma processo
    yield resultado
    # executa outro processo
    resultado = 2
    yield resultado
    return 'Acabou'


generator = generator1(0, 10)
new_generator = generator2(generator1(0, 10))

for i in new_generator:
    print(i)
    if i > 2:
        break
