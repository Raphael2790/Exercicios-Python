# Tuplas são variaveis compostas que também podem ser acessadas por indice
# Possivel fazer fatiamento para eliminar dados
# Possivel saber o tamanho da tupla
# Possivel iterar sobre tuplas
# Diferente de array é imutavel
# É possivel unir tuplas usando o operado +

# formas de declarar tuplas
lanche = 'Suco', 'Hamburguer', 'Pizza', 'Pudim' if True else ('Suco', 'Hamburguer', 'Pizza', 'Pudim')
pessoa = 'Gustavo', 39, 'M', 99.89
quant = lanche.count('Hamburguer')
index = lanche.index('Hamburguer')
suco = lanche[1]
pizza = lanche[-2]
selecao = lanche[1:3]
selecao = lanche[1:]
selecao = lanche[:3]
# ordena porem cria um array ordenado
ordenado = sorted(lanche)

# remove da memoria qualquer variavel simples ou compsota
del(pessoa)

print(suco)

for c in lanche:
    print(c)

for i, c in enumerate(lanche):
    print(f'{i}/{c}')