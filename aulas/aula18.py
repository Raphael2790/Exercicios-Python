pessoa = list()
pessoa.append('Pedro')
pessoa.append(20)
galera = list()
dado = list()
# cria uma cópia da lista [:]
galera.append(pessoa[:])

for p in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
