print('=' * 30)
print('BANCO CEV')
print('=' * 30)

notas = [1, 5, 10, 50, 100]
nota_cinq = 0
nota_dez = 0
nota_um = 0
nota_cem = 0
nota_cinco = 0
valor_saque = int(input('Qual valor voce deseja sacar? '))
index = len(notas)-1
restante = valor_saque

while True:
    nota_atual = notas[index]
    while (restante - nota_atual) > -1:
        restante -= nota_atual
        if nota_atual == 100:
            nota_cem += 1
        if nota_atual == 50:
            nota_cinq += 1
        if nota_atual == 10:
            nota_dez += 1
        if nota_atual == 5:
            nota_cinco += 1
        if nota_atual == 1:
            nota_um += 1
    if restante == 0:
        break
    else:
        index -= 1
        if index < 0:
            break

print(f'Total de {nota_cem} cédulas de R$100')
print(f'Total de {nota_cinq} cédulas de R$50')
print(f'Total de {nota_dez} cédulas de R$10')
print(f'Total de {nota_cinco} cédulas de R$5')
print(f'Total de {nota_um} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
