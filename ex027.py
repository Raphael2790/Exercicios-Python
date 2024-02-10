nome = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome.split(" ")
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[len(nome_separado)-1]

print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {primeiro_nome}")
print(f"Seu ultimo nome é {ultimo_nome}")
