times = ('Palmeiras', 'Gremio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Atlético-PR',
        'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
        'Santos', 'Goias', 'Curitiba', 'America-MG')
primeiros = times[:5]
ultimos = times[-4:]
ordem = sorted(times)
pos = times.index('Curitiba')

print('-='*30)
print(f'Lista de times do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {primeiros}')
print('-='*30)
print(f'Os 4 últimos são: {ultimos}')
print('-='*30)
print(f'Times em ordem alfabética: {ordem}')
print('-='*30)
print(f'O Curitiba está na {pos+1}º posição')
