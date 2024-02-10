nome = str(input("Digite seu nome completo: ")).strip()
quantidade_letras = len(nome.replace(" ", ""))
primeiro_nome = nome.split(" ")[0]

print("Analisando seu nome ...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {quantidade_letras} letras")
print(f"Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras")
