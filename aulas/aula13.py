# c representa o index
# terceiro parametro do range representa o incremento
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for c in range(inicio, fim+1, passo):
    print(c)
