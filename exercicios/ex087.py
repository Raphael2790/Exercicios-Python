nova_matriz = [[], [], []]
soma_pares = 0
soma_terceira_coluna = 0
maior_numero_segunda_linha = 0

for i in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {c}]: '))
        if n % 2 == 0:
            soma_pares += n
        if c == 2:
            soma_terceira_coluna += n
        if i == 1:
            if n > maior_numero_segunda_linha:
                maior_numero_segunda_linha = n
        nova_matriz[i].append(n)

print('-='*30)
for i in range(0, 3):
    if i > 0:
        print('\n')
    for j in range(0, 3):
        print(f'[{nova_matriz[i][j]:^5}]', end=' ')
print('\n')
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_numero_segunda_linha}')
