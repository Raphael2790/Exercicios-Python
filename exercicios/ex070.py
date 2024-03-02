print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

total_compra = 0
produtos_caros = 0
preco_mais_barato = 0
nome_produto_mais_barato = ''

while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if total_compra == 0:
        preco_mais_barato = preco
        nome_produto_mais_barato = nome_produto
    else:
        if preco < preco_mais_barato:
            preco_mais_barato = preco
            nome_produto_mais_barato = nome_produto
    total_compra += preco
    if preco > 1000:
        produtos_caros += 1
    continuar = ' '
    while continuar not in 'nNSs':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break

print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {produtos_caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto_mais_barato} que custa R${preco_mais_barato:.2f}')
