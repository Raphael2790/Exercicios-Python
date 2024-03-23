def imprime_info():
    jog = nome
    num_gol = 0
    if nome.isspace() or nome == '':
        jog = '<desconhecido>'
    if gols.isnumeric():
        num_gol = int(gols)
    print(f'O jogador {jog} fez {num_gol} gol(s) no campeonato')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
imprime_info()
