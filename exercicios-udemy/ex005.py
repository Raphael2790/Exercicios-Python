import json

CAMINHO_ARQUIVO = 'ex005.json'


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Raphael', 'Santos')
p2 = Pessoa('Lucas', 'Silva')
p3 = Pessoa('Miguel', 'Silva')

# necessário pegar o dicionário de proriedades da classe para converter em json
pessoas = [vars(p1), vars(p2), vars(p3)]


def create_file():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(pessoas, arquivo, ensure_ascii=False, indent=2)


# só executa se este arquivo for o arquivo que iniciou a execução
# evitando que um import acione essa função
if __name__ == '__main__':
    create_file()
