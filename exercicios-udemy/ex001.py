def criar_multiplicador(multiplicador):
    def calcular(numero):
        return numero * multiplicador
    return calcular


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(3))
print(triplicar(4))
print(quadruplicar(5))