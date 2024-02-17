print('='*10 + ' LOJAS GUANABARA ' + '='*10)

total_compra = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

valor_a_pagar = total_compra

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor_a_pagar = valor_a_pagar - (valor_a_pagar * 10 / 100)
elif opcao == 2:
    valor_a_pagar = valor_a_pagar - (valor_a_pagar * 5 / 100)
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valor_a_pagar = valor_a_pagar + (valor_a_pagar * 20 / 100)
    print(f'Sua compra será parcelada em {parcelas}x de {(valor_a_pagar / parcelas):.2f} COM JUROS')
else:
    total_compra = 0
    print('Opção inválida! Tente novamente')

print(f'Sua compra de R${total_compra} vai custar R${valor_a_pagar} no final.')
