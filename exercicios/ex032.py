from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))

if ano == 0:
    ano = date.today().year
    print(ano)

resto_divisao_por_quatro = ano % 4
resto_divisao_por_cem = ano % 100

if resto_divisao_por_quatro == 0 and resto_divisao_por_cem != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} não é BISSEXTO')
