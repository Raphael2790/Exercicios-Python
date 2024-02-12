print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

l = [s1, s2, s3]
l.sort()

soma_lados_menores = l[0] + l[1]
maior_lado = l[2]

if soma_lados_menores > maior_lado:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
