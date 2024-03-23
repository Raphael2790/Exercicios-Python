def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param valores: uma ou mais notas dos alunos
    :param sit: valor opcional, indica se deve mostrar a situação da turma
    :return: dicionário com varias informações da turma
    """
    aluno = dict()
    maior = max(valores)
    menor = min(valores)
    total = len(valores)
    media = sum(valores) / total

    aluno['total'] = total
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = media

    if sit:
        if media <= 6:
            aluno['situacao'] = 'RUIM'
        elif media >= 7:
            aluno['situacao'] = "BOA"
        else:
            aluno['situacao'] = 'RAZOAVEL'
    return aluno


res = notas(5.5, 2.5, 10, 6.5, sit=True)
print(res)
