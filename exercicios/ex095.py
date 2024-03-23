jogador = dict()
time = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['gols'] = list()
    jogador['total_gols'] = 0
    qtd_partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    for p in range(0, qtd_partidas):
        gols = int(input(f'Quantos gols na partida {p+1}? '))
        jogador['gols'].append(gols)
        jogador['total_gols'] += gols
    time.append(jogador.copy())
    resp = str(input('Deseja continuar? [S/N]'))
    while resp not in 'sSnN':
        print('Erro! A resposta dever ser S ou N')
        resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'nN':
        break

print('-='*40)
print('cod  nome       gols       total')
print('-'*20)
for c, j in enumerate(time):
    print(f'{c}  {j["nome"]}       {j["gols"]}       {j["total_gols"]}')
print('-'*20)

while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para sair)'))
    if codigo == 999:
        break
    if codigo <= len(time) - 1:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[codigo]["nome"]}: ')
        for i, g in enumerate(time[codigo]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
        print('-'*30)
    else:
        print('Codigo jogador invalido. Tente novamente')

print('<<< ENCERRANDO... >>>')
