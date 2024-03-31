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
else:
    # Executa apenas senão houve exceção
    print(f'O resultado é {r}')
finally:
    print('Programa finalizado!')
