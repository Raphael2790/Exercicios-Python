salario = float(input("Qual é o salário do Funcionário? R$"))
aumento = salario*(15/100)
novo_salario = salario + aumento
print(f"Un funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber o valor R${novo_salario:.2f}."
      f"\nO aumento foi de R${aumento:.2f}.")
