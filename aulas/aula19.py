# Dicionarios são valores por referencia que utilizam notação chave:valor mutaveis

pessoa = dict(nome='Raphael', idade=20)

pessoa['sexo'] = 'M'

del pessoa['sexo']

valores = pessoa.values()
chaves = pessoa.keys()

pessoa_copia = pessoa.copy()