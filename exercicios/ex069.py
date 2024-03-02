pessoas_maior_idade = homens = mulheres_menores_idade = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA:')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mMfF':
        sexo = str(input('Sexo: [M/F]'))
    if sexo in 'mM':
        homens += 1
    if idade > 18:
        pessoas_maior_idade += 1
    if sexo in 'fF' and idade < 20:
        mulheres_menores_idade += 1
    continuar = ' '
    while continuar not in 'sSNn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'nN':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas_maior_idade}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menores_idade} mulheres com menos de 20 anos')
