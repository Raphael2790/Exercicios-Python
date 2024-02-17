nome = str(input('Qual o seu nome? '))

if nome == 'Raphael':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que belo nome feminino')
else:
    print('Seu nome é bem normal!')

print(f'Tenha um bom dia, {nome}!')
