def soma(a, b):
    print(a + b)


# função com empacotamento de parametros
# utilizado quando não sabemos quantos parametros iremos receber
# como se fosse uma tupla sendo recebida, podemos usar todas operaçoes de tuplas
# logo o empacotamento é imutavel
# todos valores passados por parametro são passados por referencia
def contador(* num):
    print(num)
    print(len(num))


soma(2, 4)

# podemos nomear parametros
soma(b=6, a=1)

contador(1, 2, 4, 9)
contador(1, 2, 4, "9")
