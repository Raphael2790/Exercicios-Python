print('Gerador de PA')
print('-='*10)

inicio = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
parar = False
cont = 10
quant = 0

while cont > 0:
    print(inicio, end=' -> ')
    inicio += razao
    cont -= 1
    quant += 1
    if cont == 0:
        print('PAUSA', end='')
        prox_seq = int(input('\nQuantos termos você quer mostrar a mais? '))
        cont += prox_seq

print(f'Progressão finalizada com {quant} termos mostrados')
