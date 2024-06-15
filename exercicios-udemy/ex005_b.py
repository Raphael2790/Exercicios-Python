import json
from ex005 import Pessoa, CAMINHO_ARQUIVO

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    print(p1.nome, p1.sobrenome)