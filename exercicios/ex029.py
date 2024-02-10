velocidade = int(input('Qual a velocidade atual do carro? '))
limite_velocidade = 80
multa_por_km_excedido = 7.00

if velocidade > limite_velocidade:
    excedido = float(velocidade - limite_velocidade)
    multa = multa_por_km_excedido * excedido
    print(f'MULTADO! Você excedeu o limite permitido que é de {limite_velocidade}Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')
