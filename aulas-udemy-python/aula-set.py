# Sets são conjuntos de dados que não permitem duplicidade entre eles, são permitidos apenas dos imutáveis
# Não garantem a ordem dos dados
# São iteraveis
# Criação de set via classe
s1 = set('Raphael')
# Criação de set via notação
s2 = {1, 2, 4}

print(s1)
print(4 in s1)

# limpa
s1.clear()
# adiciona
s1.add('Raphael')
# atualiza
s1.update((1, 2, 3, 4))
# discarta um valor existente
s1.discard('Raphael')

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Retorna a união dos conjuntos sem duplicidade
s3 = s1 | s2
# Intersecção entre os 2 conjuntos
s3 = s1 & s2
# Diferença entre conjuntos consiferando apenas o set da esquerda
s3 = s1 - s2
# Diferença simétrica, elementos que são unicos nos 2 conjuntos
s3 = s1 ^ s2
