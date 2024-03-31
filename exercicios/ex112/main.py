from moeda import resumo
from textos import leia_dinheiro

preco = leia_dinheiro('Digite o preço: R$')
resumo(preco, 35, 22)
