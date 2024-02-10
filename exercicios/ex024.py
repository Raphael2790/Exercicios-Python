cidade = str(input("Em que cidade você nasceu? ")).strip().lower()
nome_inicio = "santo"
primeiro_nome_cidade = cidade.split(" ")[0]
print(nome_inicio in primeiro_nome_cidade)
