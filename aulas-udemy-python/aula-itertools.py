from itertools import combinations, product, permutations, groupby

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['algodão', 'poliester'],
    ['masculino', 'feminina'],
    ['p', 'm', 'g']
]

# cria uma combinação sem repetições nos grupos
print(list(combinations(pessoas, 2)))
# cria uma combinação com reptições e troca de ordem
print(list(permutations(pessoas, 2)))
# cria uma combinação unica entre valores elementos entre listas
print(list(product(camisetas)))


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'])
# para realizar o agrupamento via group by o iteravel precisa estar odenado
grupos = groupby(alunos_ordenados, key=lambda aluno: aluno['nota'])

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))
