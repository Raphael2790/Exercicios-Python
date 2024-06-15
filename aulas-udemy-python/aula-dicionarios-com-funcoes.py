tarefas = []
tarefas_refazer = []


def listar(tarefas):
    pass


def desfazer(tarefas, tarefas_desfazer):
    ...


def refazer(tarefas, tarefas_refazer):
    pass


def adicionar(tarefa, tarefas):
    pass


selecao = input('Digite um comando')

comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
    'refazer': lambda: refazer(tarefas, tarefas_refazer),
    'adicionar': lambda: adicionar("Nova tarefa", tarefas)
}
comando = comandos.get(selecao) if comandos.get(selecao) is not None else comandos['adicionar']

comando()
