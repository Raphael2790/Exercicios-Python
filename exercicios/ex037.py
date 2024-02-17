num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    conversao = bin(num)
    print(f'{num} convertido para BINÁRIO é igual a {conversao[2:]}')
elif opcao == 2:
    conversao = oct(num)
    print(f'{num} convertido para OCTAL é igual a {conversao[2:]}')
elif opcao == 3:
    conversao = hex(num)
    print(f'{num} convertido para HEXADECIMAL é igual a {conversao[2:]}')
else:
    print('Opção inválida. Tente novamente')
