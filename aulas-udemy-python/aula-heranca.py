class Pessoa:
    cpf = '0099898'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    # sobrescreve o metodo da super classe
    def falar_nome_classe(self):
        print('Classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)
        super().falar_nome_classe()


class Aluno(Pessoa):
    cpf = '1918181'


cliente = Cliente('Raphael', 'Santos')
aluno = Aluno('Miguel', 'Silva')
cliente.falar_nome_classe()


class A:
    ...
    
    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(B,A):
    ...

    def quem_sou(self):
        print('C')


c = C()
# resolução de chamadas de metodos
print(C.mro())
