frase = str(input('Digite uma frase: ')).strip().lower()
letra_procurada = 'a'
repete = frase.count(letra_procurada)
primeira_ocorrencia = frase.find(letra_procurada) + 1
ultima_ocorrencia = frase.rfind(letra_procurada) + 1
print(f"A letra A aparece {repete} vezes na frase")
print(f"A primeira letra A apareceu na posição {primeira_ocorrencia}")
print(f"A última letra A apareceu na posição {ultima_ocorrencia}")
