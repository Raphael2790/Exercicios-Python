class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar_erro():
    raise MeuError('a', 'b', 'c').add_note('Mais alguma coisa no erro')


try:
    levantar_erro()
except (MeuError, ZeroDivisionError) as error:
    print(error)
    print(error.__class__.__name__)
    print()
    raise OutroError('Vou lançar de novo') from error
