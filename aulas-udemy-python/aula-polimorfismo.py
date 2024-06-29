from abc import abstractmethod, ABC


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'E-mail: Enviando notificação {self.mensagem}')
        return True


class NotificacaoSms(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS: Enviando notificação {self.mensagem}')
        return False


def notificar(notificacao: Notificacao):
    sucesso = notificacao.enviar()

    if sucesso:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificar(NotificacaoSms('teste SMS'))
notificar(NotificacaoEmail('teste email'))
