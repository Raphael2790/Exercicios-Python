class Multiplica:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna


# decora uma função adicionando comportamento da classe no resultado
@Multiplica(10)
def soma(x, y):
    return x + y


resultado_soma = soma(2, 4)
print(resultado_soma)
