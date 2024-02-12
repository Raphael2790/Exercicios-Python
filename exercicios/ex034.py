salario = float(input('Qual é o salário do funcionário? '))
salario_limite = 1250
novo_salario = salario * 1.15 if salario < salario_limite else salario * 1.10
print(f'Quem ganhava R${salario} passa a ganhar R${novo_salario} agora.')
