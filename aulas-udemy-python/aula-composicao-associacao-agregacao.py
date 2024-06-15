class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self.ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Raphael')
caneta = FerramentaDeEscrever('Caneta')
# composição escritor usa caneta - Associação
escritor.ferramenta = caneta


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.__produtos = []

    def total(self):
        return sum([p.preco for p in self.__produtos])

    def listar_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.preco)
        print()

    def adicionar_produto(self, *produtos):
        self.__produtos.extend(produtos)
        # self.__produtos += produtos


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 4.50), Produto('Lapis', 2.20)
# carrinho possui produtos porem ambos existem sem a dependencia - Agregação
carrinho.adicionar_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)


# cliente possui enderecos e enderecos não existe sem cliente - Composição
cliente = Cliente('Raphael')
cliente.inserir_endereco('Rua Logo ali', 1019)
cliente.listar_enderecos()