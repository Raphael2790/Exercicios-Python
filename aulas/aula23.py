import aula06

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (TypeError, ValueError) as erro:
    print(f'Aconteceu o seguinte erro: {erro.__cause__}')
except ZeroDivisionError as division:
    print(f'Aconteceu o seguinte erro: {division.__class__}')
except Exception as generico:
    print(f'Aconteceu um erro: {generico.__cause__}')
except KeyError as key:
    print(f'Aconteceu o seguinte erro: {key.__class__}')
    raise
else:
    # Executa apenas senão houve exceção
    print(f'O resultado é {r}')
finally:
    print('Programa finalizado!')

print(f'Este modulo é o {__name__}')
n1 = aula06.n1


# Levantar exceção
raise TypeError('Aconteceu um erro de tipo')