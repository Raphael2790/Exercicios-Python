from numeros import dobro, metade, aumentar
from textos import pergunta_preco
from moeda import formatar_moeda

preco = pergunta_preco('Digite o preço: R$')

print(f'A metade de R${formatar_moeda(preco)} é R${formatar_moeda(metade(preco))}')
print(f'O dobro de R${formatar_moeda(preco)} é R${formatar_moeda(dobro(preco))}')
print(f'Aumentando 10%, temos R${formatar_moeda(aumentar(preco, 10))}')

