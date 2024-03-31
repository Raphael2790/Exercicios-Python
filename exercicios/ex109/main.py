from numeros import dobro, metade, aumentar, diminuir
from textos import pergunta_preco
from moeda import formatar_moeda

preco = pergunta_preco('Digite o preço: R$')

print(f'A metade de R${formatar_moeda(preco)} é R${metade(preco, True)}')
print(f'O dobro de R${formatar_moeda(preco)} é R${dobro(preco, True)}')
print(f'Aumentando 10%, temos R${aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos R${diminuir(preco, 10, True)}')

