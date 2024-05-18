lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Raphael'}
]

for index, item in enumerate(lista):
    if isinstance(item, str):
        print('Texto encontrado', index)

    if isinstance(item, (int, float)):
        print('Número encontrado', index)

    if isinstance(item, bool):
        print('Booleano', index)

    if isinstance(item, set):
        print('SET encontrado', index)

