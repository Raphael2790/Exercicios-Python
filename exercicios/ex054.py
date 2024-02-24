from datetime import date

maior_idade = 0
menor_idade = 0

ano_atual = date.today().year

for c in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    if (ano_atual - ano_nasc) >= 21:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'Ao todo tivemos {maior_idade} pessoas maiores de idade')
print(f'E também tivemos {menor_idade} pessoas menores de idade')
