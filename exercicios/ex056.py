soma = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_abaixo_idade = 0

for i in range(1, 5):
    print(f'----- {i}° PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    soma += idade
    if sexo in 'mM' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    elif sexo in 'fF' and idade < 20:
        mulheres_abaixo_idade += 1

print(f'A média de idade do grupo é de {(soma/5):.1f}')
print(f'O homem mais velho do grupo tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todo são {mulheres_abaixo_idade} mulheres com menos  de 20 anos')
