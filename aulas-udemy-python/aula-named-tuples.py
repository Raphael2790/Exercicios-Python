from typing import NamedTuple
from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'],
                   defaults=['VALOR', 'NAIPE'])

carta = Carta('10', 'espadas')


# criação de namedtuple via herança
class Carro(NamedTuple):
    nome: str
    marca: str
    portas: int
