# importação de modulos criados qualquer arquivo py é um modulo
# import modules.uteis as uteis
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
