def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


# cria um decorador que altera o comportamento de um metodo da classe
def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def decora_nome(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'São Paulo' in resultado:
            return 'É o seu time do coração'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    @decora_nome
    def falar_nome(self):
        return f'O nome do time é {self.nome}'

    # Faz uma instancia de classe poder ser invocada
    def __call__(self, *args, **kwargs):
        print(f'O time {self.nome} está sendo escalado')


time = Time('São Paulo')
print(time)
print(time.falar_nome())
time()
