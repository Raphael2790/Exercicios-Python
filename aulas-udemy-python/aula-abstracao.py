from abc import ABC, abstractmethod
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


# para uma classe ser abstrata ela precisa herdade de ABC e possuir um metodo marcado como abstrato
# Ao criar a instancia de uma classe abstrata apos isso sera lançado um erro
class Log(ABC):

    # metodo protegido abstrato
    @abstractmethod
    def _log(self, mensagem):
        ...

    def log_error(self, mensagem):
        return self._log(f'Error: {mensagem}')

    def log_success(self, mensagem):
        return self._log(f'Success: {mensagem}')


class LogFileMixin(Log):

    def _log(self, mensagem):
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(mensagem)
            file.write('\n')


class LogPrintMixin(Log):

    def _log(self, mensagem):
        print(f'{mensagem} ({self.__class__.__name__})')


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


# adicionado funcionalidades de log usando herança multipla
# ideal é que classe que adicionam funcionalidades vira herança venham sempre após a classe base
# prefira composição sempre que possivel via construtor ou metodos
class SmartPhone(Eletronico, LogPrintMixin):

    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)


if __name__ == '__main__':
    logger = LogPrintMixin()
    logger.log_success('Sucesso')

    iphone = SmartPhone('iPhone')
    iphone.ligar()
