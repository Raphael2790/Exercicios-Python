maior_peso = 0.00
menor_peso = 0.00

for i in range(0, 5):
    peso = float(input(f'Peso da {i+1}° pessoa:'))
    if peso > maior_peso:
        maior_peso = peso
    elif menor_peso == 0.00 or peso < menor_peso:
        menor_peso = peso

print(f'O maior peso lido foi de {maior_peso:.1f}Kg')
print(f'O menor peso lido foi de {menor_peso:.1f}Kg')
