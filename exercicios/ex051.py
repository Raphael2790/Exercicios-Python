print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = termo + (10 - 1) * razao

for c in range(termo, decimo_termo + razao, razao):
    print(c, end=' -> ')
print(' -> ACABOU')
