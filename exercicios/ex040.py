n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

print(f'Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {media:.2f}')

if media >= 7.0:
    print('O aluno está APROVADO')
elif 5.0 <= media <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
elif media < 5.0:
    print('O aluno está REPROVADO')
