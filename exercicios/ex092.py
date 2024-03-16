from datetime import datetime

funcionario = dict()
ano_atual = datetime.today().year

funcionario['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
funcionario['idade'] = ano_atual - ano_nascimento
funcionario['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if funcionario['ctps'] != 0:
    funcionario['contratacao'] = int(input('Ano de Contratação: '))
    funcionario['salario'] = float(input('Salário: R$'))
    funcionario['aposentadoria'] = funcionario['idade'] + (35 - (ano_atual - funcionario['contratacao']))

print('-='*30)

for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')
