from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação : MIRIM')
elif idade <= 14:
    print('Classificação : INFANTIL')
elif idade <= 19:
    print('Classificação : JUNIOR')
elif idade <= 25:
    print('Classificação : SÊNIOR')
elif idade > 25:
    print('Classificação : MASTER')
