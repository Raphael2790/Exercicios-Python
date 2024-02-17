s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

lista = [s1, s2, s3]
lista.sort()
soma_lados_menores = lista[0] + lista[1]
maior_lado = lista[2]
pode_formar_triangulo = soma_lados_menores > maior_lado

if pode_formar_triangulo:
    if s1 == s2 == s3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
