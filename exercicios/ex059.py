from time import sleep

sair = False
trocar_numeros = False
n1 = 0
n2 = 0

while not sair:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    trocar_numeros = False
    while not trocar_numeros:
        print('    [1] somar')
        print('    [2] multiplicar')
        print('    [3] maior')
        print('    [4] novos números')
        print('    [5] sair do programa')
        opcao = int(input('>>>>> Qual é a sua opção?'))
        if opcao == 5:
            sair = True
            trocar_numeros = True
            print('Finalizando...')
            print('=-=' * 10)
            print('Fim do programa! Volte sempre!')
        elif opcao == 1:
            print(f'A soma entre {n1} + {n2} é {n1+n2}')
            print('=-=' * 10)
        elif opcao == 2:
            print(f'A multiplicacao entre {n1} x {n2} é {n1*n2}')
            print('=-=' * 10)
        elif opcao == 3:
            if n1 > n2:
                print(f'Entre {n1} e {n2} o maior é {n2}')
                print('=-=' * 10)
            elif n1 < n2:
                print(f'Entre {n2} e {n2} o maior é {n1}')
                print('=-=' * 10)
            else:
                print('São iguais')
                print('=-=' * 10)
        elif opcao == 4:
            print('Informe os números novamente:')
            trocar_numeros = True
        else:
            print('Opção inválida. Tente novamente')
            print('=-=' * 10)
        sleep(1)
        