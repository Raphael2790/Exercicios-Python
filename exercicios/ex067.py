cont = 1

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    cont = 1
    print('-' * 30)
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
