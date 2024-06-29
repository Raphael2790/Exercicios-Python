import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA', 'CIMA', 'BAIXO'])


def mover(direcao : Direcoes):
    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes(2))
mover(Direcoes['CIMA'])


class Status(enum.Enum):
    PENDENTE = 1
    EM_EXECUCAO = 2
    CONCLUIDO = enum.auto()


print(Status.CONCLUIDO)


class Banco:
    def __init__(self, contas, clientes, agencias):
        self.contas: list[int] | None = contas or []
        self.clientes: list[str] | None = clientes or []
        self.agencias: list[int] = agencias or []
