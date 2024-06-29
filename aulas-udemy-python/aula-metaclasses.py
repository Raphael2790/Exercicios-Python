# cria uma classe com nome de Foo através de um metadado
Foo = type('Foo', (object,), {'nome': 'Raphael'})

f = Foo()
print(f.nome)


# criando sua propria meta classe herdando da meta classes type
class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('Criando a classe')
        cls = super().__new__(mcs, name, bases, dct)
        cls.numero = 1234
        return cls

    def __call__(self, *args, **kwargs):
        print('Criando a instancia')
        instancia = super().__call__(*args, **kwargs)
        return instancia


# definindo a classe pessoa mudando o meta type dela base
class Pessoa(metaclass=Meta):
    ...
