def mostra_cabecalho():
    print('~'*30)
    print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
    print('~' * 30)


def mostra_fim():
    print('~'*30)
    print(f'{"Até logo!":^30}')
    print('~' * 30)


def mostra_mensagem_busca(busca):
    print('~' * 40)
    print(f'{f"Acessando o manual do comando '{busca}'":^30}')
    print('~' * 40)


def analisa_instrucao():
    from time import sleep
    while True:
        mostra_cabecalho()
        func = str(input('Função ou biblioteca >'))
        sleep(1)
        if func.lower() == 'fim':
            break
        mostra_mensagem_busca(func)
        sleep(1)
        help(func)
    mostra_fim()


analisa_instrucao()
