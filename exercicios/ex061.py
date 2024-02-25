print('Gerador de PA')
print('-='*10)

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0

while cont < 10:
    print(inicio, end=' -> ')
    inicio += razao
    cont += 1
print('FIM')
