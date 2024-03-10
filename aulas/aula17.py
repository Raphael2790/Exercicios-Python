# Listas
# listas são mutaveis
# lista é um valor por referencia

num = [2, 5, 9, 1]
num.sort()
num.sort(reverse=True)
qtd_elem = len(num)

# colocar item no final da lista, o python cuida do aumento do array
num.append(7)
# adiciona no indice o valor especificado
num.insert(2, 0)

num.pop()
num.pop(5)
# remove apenas o primeiro elemento encontrado
num.remove(2)

valores = list(range(4, 11))

# cria uma copia da lista
b = valores[:]

print(num)
