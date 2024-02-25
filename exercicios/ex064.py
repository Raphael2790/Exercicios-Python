parar = False
soma = 0
count = 0

while not parar:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        parar = True
    else:
        soma += n
        count += 1

print(f'Você digitou {count} e a soma entre eles foi {soma}')
