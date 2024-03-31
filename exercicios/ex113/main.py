from numeros import leia_int, leia_float

inteiro = 0
flutuante = 0

try:
    inteiro = leia_int('Digite um número inteiro: ')
    flutuante = leia_float('Digite um número real: ')
except KeyboardInterrupt:
    print('\033[0;31mO usuário interrompeu a execução do programa\033[m')
except Exception as erro:
    print(f'Aconteceu um erro inesperado: {erro.__cause__}')
finally:
    print(f'O valor inteiro ditado foi {inteiro} e o real foi {flutuante}')
