frase = "   Curso em Video Python   "
uma_letra = frase[1]
range_letras = frase[2:10]
range_letras = frase[:10]
range_letras = frase[9:]
range_letras = frase[::3]
range_letras_intervalo = frase[2:18:2]
range_letras_intervalo = frase[2::2]

print("""Texto muito grande
que ocupa muitas linhas""")

letras_o = frase.count('o')
separar_frase = frase.split()
frase_sem_espacos = frase.strip()
frase_sem_espacos = frase.lstrip()
frase_sem_espacos = frase.rstrip()
frase_maiuscula = frase.upper()
frase_minuscula = frase.lower()
quantide_letras = len(frase)
troca_palavra = frase.replace('Python', 'Android')
verifica_seq = 'Curso' in frase
index_curso = frase.find('Curso')
index_left = frase.rfind('Python')
