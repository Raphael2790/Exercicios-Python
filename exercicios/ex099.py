def analise_valores(* numeros):
    print('-='*30)
    print('Analisando valores passados...')
    lista_numeros = sorted(numeros)
    maior = 0
    if len(numeros) > 0:
        maior = max(lista_numeros)
    for n in numeros:
        print(n, end=' ')
    print(f'Foram informados {len(numeros)} ao todo.')
    print(f'O maior valor informado foi {maior}.')


analise_valores(2, 9, 4, 5, 7, 1)
analise_valores(4, 7, 0)
analise_valores(1, 2)
analise_valores(6)
analise_valores()
