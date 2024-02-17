from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade_atual = ano_atual - ano
idade_alistamento = 18

print(f'Quem nasceu em {ano} tem {idade_atual} anos em {ano_atual}.')

if idade_atual == idade_alistamento:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade_atual < idade_alistamento:
    anos_faltando = idade_alistamento - idade_atual
    ano_alistamento = ano_atual + anos_faltando
    print(f'Ainda faltam {anos_faltando} anos para o alistamento')
    print(f'Seu alistamento será em {ano_alistamento}')
elif idade_atual > idade_alistamento:
    anos_atraso = idade_atual - idade_alistamento
    ano_alistamento = ano_atual - anos_atraso
    print(f'Você já deveria ter se alistado há {anos_atraso} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}')
