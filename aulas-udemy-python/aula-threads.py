from time import sleep
from threading import Thread, Lock


class MyThread(Thread):
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        super().__init__()

    def run(self):
        sleep(self.duracao)
        print(self.nome)


t1 = MyThread('Thread 1', 3)
t1.start()

t2 = MyThread('Thread 2', 1)
t2.start()


for i in range(10):
    sleep(1)
    print(i)


def funcao_demorada(texto, duracao):
    sleep(duracao)
    print(texto)


t3 = Thread(target=funcao_demorada, args=('Olá mundo!', 5))
t3.start()
# bloqueia a thread principal
# t3.join()

while t3.is_alive():
    print('Esperando a Thead')
    sleep(2)

print('Finalizou a thread')

class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Nosso cadeado
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)

