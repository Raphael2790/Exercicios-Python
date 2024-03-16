pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input(f'Média de {pessoa["nome"]}: '))
pessoa['situacao'] = ''

if pessoa['média'] < 5:
    pessoa['situacao'] = 'Reprovado'
elif pessoa['média'] > 7:
    pessoa['situacao'] = 'Aprovado'
else:
    pessoa['situacao'] = 'Recuperação'

print('-='*40)
for k, v in pessoa.items():
    print(f'- {k} é igual a {v}')
