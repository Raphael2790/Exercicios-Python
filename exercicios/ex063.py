n1 = 0
n2 = 1
ant = 0

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

quant = int(input('Quantos termos você quer mostrar? '))
print('~'*20)
print(n1, end=' -> ')
print(n2, end=' -> ')
while (quant - 2) > 0:
    ant = n1+n2
    print(ant, end=' -> ')
    quant -= 1
    n1 = n2
    n2 = ant
print('FIM \n')
print('~'*20)
