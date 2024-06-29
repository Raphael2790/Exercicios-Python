from dataclasses import dataclass, asdict, astuple, field


# o decorador data classes já cria o construtor com a propriedade
# define também os metodos __eq__ e __repr__
# init define se será executado o metodo __post_init__ da dataclass
# frozen define se o objeto será somente leitura

@dataclass(init=True, frozen=False)
class Pessoa:
    nome: str = field(default='Missing')
    sobrenome: str = field(default='Not set')
    idade: int = field(default=0)
    enderecos: list[str] = field(default_factory=list)

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __post__init(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


if __name__ == '__main__':
    p1 = Pessoa('Raphael', 'Santos')
    print(asdict(p1))
    print(astuple(p1))
