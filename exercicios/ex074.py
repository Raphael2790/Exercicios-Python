from random import randint

num_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = max(num_aleatorios)
menor = min(num_aleatorios)

print(f'Os valores sorteados foram: {num_aleatorios}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
