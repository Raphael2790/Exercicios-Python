from numeros import dobro, metade, aumentar
from textos import pergunta_preco

preco = pergunta_preco('Digite o preço: R$')

print(f'A metade de R${preco} é R${metade(preco)}')
print(f'O dobro de R${preco} é R${dobro(preco)}')
print(f'Aumentando 10%, temos R${aumentar(preco, 10)}')

