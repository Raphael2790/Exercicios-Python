alunos = list()
aluno = list()
notas = list()

while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    n1 = float(input('Nota 1: '))
    notas.append(n1)
    n2 = float(input('Nota 2: '))
    notas.append(n2)
    aluno.append(notas[:])
    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    res = str(input('Quer continuar? [S/N]'))
    if res in 'nN':
        break

print('-='*40)
print(f'{"No.":<4} {"Nome":<10} {"MÉDIA":>8}')
print('-'*30)

for index, aluno in enumerate(alunos):
    media = (aluno[1][0] + aluno[1][1]) / len(aluno[1])
    print(f'{index:<4} {aluno[0]:<10} {media:>8.1f}')

while True:
    indice_aluno = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if indice_aluno == 999:
        break
    if indice_aluno <= len(alunos) - 1:
        aluno_exibir = alunos[indice_aluno]
        print(f'As notas de {aluno_exibir[0]} sao {aluno_exibir[1]}')
        print('-'*30)

print('FINALIZANDO...')
print('<<< Volte Sempre >>>')
