import string
from datetime import date


class MyTemplate(string.Template):
    delimiter = "%"


texto = '''
    Olá $nome, como vai? Sua consulta no endereço: $endereco, vai ser
    realizada no dia $data.
    
    Agradecemos desde já
    $empresa
'''

dados = {
    'nome': 'Raphael',
    'endereco': 'Rua Logo Ali, n° 100',
    'data': date(2024, 12, 1).strftime('%d/%m/%Y'),
    'empresa': 'Consultas LTDA'
}

print(string.Template(texto).substitute(dados))

# caso os dados não existam no dicionario será utilizado o caracter de substituição
novo_texto = string.Template(texto).safe_substitute(dados)

MyTemplate(texto).substitute(dados)
