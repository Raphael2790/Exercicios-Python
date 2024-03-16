matriz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))

print('-='*30)
for i in range(0, 3):
    if i > 0:
        print('\n')
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
print('\n')
print('-='*30)
