class Ponto:
    # sobrescreve a criação da instancia da classe
    # caso queira executar algo ao iniciar a classe
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # metodo que será invocado caso __str__ não seja sobrescrito
    def __repr__(self):
        class_name = type(self).__name__
        # Ao utilizar !r informamos que queremos a representação dos tipos inclusos
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    # def __str__(self):
    #    return f'(x={self.x!s}, y={self.y!s}, z={self.z!s})'

    # todos operadores podem ser sobrescritos
    # sobrescrita operador '+' para ser utilizado entre classes Ponto
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other) -> bool:
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


p1 = Ponto(10, 6)
p2 = Ponto(12, 10)
print(p1 + p2)
print(p1 > p2)
