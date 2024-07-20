from csv import reader, DictReader, writer, DictWriter
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    # le em formato de lista a linha
    leitor = reader(arquivo)
    _ = next(leitor)

    for item in leitor:
        print(item)

with open(CAMINHO_CSV, 'r') as arquivo:
    # le em formato de dicionario a  linha
    leitor = DictReader(arquivo)
    _ = next(leitor)

    for item in leitor:
        print(item)

clientes = [
    {'Nome': 'João', 'Endereço': 'Rua Logo Ali'},
    {'Nome': 'Maria', 'Endereço': 'Rua Bem Longe'}
]

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = clientes[0].keys()

    escritor = writer(arquivo)
    escritor.writerow(nome_colunas)

    for item in clientes:
        escritor.writerow(item.values())

with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = clientes[0].keys()
    escritor = DictWriter(arquivo, fieldnames=nome_colunas)

    for item in clientes:
        escritor.writerow(item)
