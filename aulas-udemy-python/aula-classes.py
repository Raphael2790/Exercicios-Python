class Pessoa:
    saudacao = 'Que bom te conhecer'

    # metodo acionado ao criar a instancia com se fosse um construtor
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def comprimentar(self):
        print(f'Olá eu sou o {self.nome}, qual seu nome? {Pessoa.saudacao}')

    # metodo fabrica que cria uma instancia
    # decorator class metodo vai colocar o molde de pessoa no primeiro parametro
    # como se fosse um metodo estatico porem com acesso a classe
    @classmethod
    def criar_pessoa_com_idade(cls, nome, idade):
        return cls(nome, idade)

    @staticmethod
    def calcula_ano_nascimento(idade_pessoa, ano_atual):
        return ano_atual - idade_pessoa


p1 = Pessoa('Raphael', 'Santos')
# similar ao javascript é possível criar propriedades em objetos dinamicamente
# p1.nome = 'Raphael'
# p1.sobrenome = 'Santos'

p1.comprimentar()

# retorna todas propriedades da instancia
print(p1.__dict__)
print(vars(p1.__dict__))

Pessoa.comprimentar(p1)
Pessoa.criar_pessoa_com_idade('Raphael', 39)
ano = Pessoa.calcula_ano_nascimento(35, 2024)

print(p1.nome)
