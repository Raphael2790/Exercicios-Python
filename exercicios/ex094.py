pessoa = dict()
cadastros = list()
soma_idade = 0
mulheres = list()
media_idade = 0

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: '))
    while pessoa['sexo'] not in 'mMfF':
        print('ERRO!. Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    if pessoa['sexo'] in 'fF':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    cadastros.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N]'))
    while resp not in 'sSnN':
        print('ERRO!. Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N]'))
    if resp in 'nN':
        break

media_idade = soma_idade / len(cadastros)

print('-='*30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for m in mulheres:
    print(m, end=' ')
print(f'\nD) Lista de pessoas que estão acima da média: ')
for p in cadastros:
    if p['idade'] > media_idade:
        print(f'nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']};')

print('<<< ENCERRADO >>>')