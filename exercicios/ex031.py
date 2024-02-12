km = float(input('Qual a distência de sua viagem? '))
preco_normal = 0.50
preco_desconto = 0.45
faixa_km_desconto = 200

print(f'Você está prestes a começar uma viagem de {km}Km.')
preco_viagem = preco_normal * km if km <= faixa_km_desconto else preco_desconto * km
print(f'E o preço da sua passagem será de R${preco_viagem:.2f}')

