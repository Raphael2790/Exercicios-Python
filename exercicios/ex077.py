palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

vogais = ('a', 'e', 'i', 'o', 'u', 'ão')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(f'{letra.lower()}', end=' ')
