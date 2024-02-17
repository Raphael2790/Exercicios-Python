valor_casa = float(input('Valor da casa: '))
salario_comprador = float(input('Salário do comprador: '))
anos_financiamento = int(input('Quantos anos de finaciamento? '))
meses_financiamento = anos_financiamento * 12
prestacao = valor_casa / meses_financiamento
salario_base_financiamento = salario_comprador * 0.30

print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_financiamento} anos a prestação será de R${prestacao:.2f} mensal.')

if salario_base_financiamento > prestacao:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO')
