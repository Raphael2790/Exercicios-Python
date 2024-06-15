

# Função decoradora
def fabrica_decoradores(a=None, b=None, c=None):
    print('Executou')
    def cria_funcao(func):
        def interna(*args, **kwargs):
            print('Vou te decorar')
            print(a, b, c)
            for arg in args:
                e_string(arg)
            for key, item in kwargs.items():
                print(key, item)
            resultado = func(*args, **kwargs)
            print(f'O seu resultado foi {resultado}')
            print('Ok, agora vc foi decorada')
            return resultado
        return interna
    return cria_funcao


# utilizacao decorador
@fabrica_decoradores(4, 5, 6)
@fabrica_decoradores(1, 2, 3)
def inverte_string(string, name="Raphael"):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Deve ser um texto')


texto = inverte_string('Raphael', name='Junio')

print(texto)
