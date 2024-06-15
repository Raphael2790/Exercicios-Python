class Caneta:
    _propriedade_protected = 'Isso é protected'
    __propriedade_private = 'Isso é privado'

    def __init__(self, cor, cor_tampa):
        self.__cor = cor
        self.__cor_tampa = cor_tampa
        self._atributo_protected = 'Atributo protected'
        self.__atributo_private = 'Atributo private'

    # getter
    @property
    def cor(self):
        return self.__cor

    # setter
    @cor.setter
    def cor(self, value):
        self.__cor = value

    # getter
    @property
    def cor_tampa(self):
        return self.__cor_tampa

    # setter
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self.__cor_tampa = valor

    @staticmethod
    def _metodo_protected(self):
        print('metodo protected')

    @staticmethod
    def __metodo_private(self):
        print('metodo private')


# definindo getter e setter praticamos o encapsulamento e pode validar/verificar valores
caneta = Caneta('Azul', 'Verde')
caneta.cor = 'Rosa'
print(caneta.cor)
