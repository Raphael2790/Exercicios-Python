soma = 0
quantidade_numeros = 0

for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        quantidade_numeros += 1

print(f'A soma de todos os {quantidade_numeros} valores solicitados é {soma}')
