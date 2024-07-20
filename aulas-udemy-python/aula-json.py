import json
from typing import TypedDict


class Pessoa(TypedDict):
    nome: str
    sobrenome: str
    enderecos: list[str]
    altura: float
    numeros: tuple
    dev: bool
    nada: None


pessoa = {
    'nome': 'Raphael',
    'sobrenome': 'Santos',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55}
    ],
    'altura': 1.7,
    'numeros': (2, 4, 57, 87),
    'dev': True,
    'nada': None
}

# escrita json
with open('aula.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2
    )

# leitura json
with open('aula.json', 'r', encoding='utf-8') as arquivo:
    retorno_json = json.load(
        arquivo
    )

# dumps é utilizado para converter um objeto em json
pessoa_json = json.dumps(pessoa, indent=2, ensure_ascii=False)
print(pessoa_json)

# loads é utilizado para converter um json em objeto
pessoa_objeto: Pessoa = json.loads(pessoa_json)
print(pessoa_objeto)
