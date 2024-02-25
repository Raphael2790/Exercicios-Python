sexo = str(input('Informe seu sexo: [M/F]'))

while sexo not in 'mMfF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))

print(f'Sexo {sexo.upper()} registrado com sucesso')
