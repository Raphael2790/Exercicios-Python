frase = input('Digite uma frase: ').strip().replace(' ', '').upper()
inversa = ''
# inversa = frase[::-1]

for c in range(len(frase)-1, -1, -1):
    inversa += frase[c]

print(f'O inverso de {frase} é {inversa}')

if frase == inversa:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palídromo')
