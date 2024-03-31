import exercicios.ex112.numeros as moeda

def formatar_moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco, aumentar, diminuir):
    print('-'*30)
    print(f'{"RESUMO VALOR":^30}')
    print('-'*30)
    print(f'Preço analisado : {moeda.formatar_moeda(preco, 'R$')}')
    print(f'Dobro do preço: {moeda.dobro(preco, True)}')
    print(f'Metade do preço: {moeda.metade(preco, True)}')
    print(f'{aumentar}% de aumento: {moeda.aumentar(preco, aumentar, True)}')
    print(f'{diminuir}% de redução: {moeda.diminuir(preco, diminuir, True)}')
    print('-'*30)
