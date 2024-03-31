from exercicios.ex112.moeda import formatar_moeda


def metade(number=0, formatar=False):
    total = number / 2
    if formatar:
        return formatar_moeda(total)
    return str(total)


def dobro(number=0, formatar=False):
    total = number * 2
    if formatar:
        return formatar_moeda(total)
    return str(total)


def aumentar(number=0, porcentagem=0, formatar=False):
    total = number + ((number * porcentagem) / 100)
    if formatar:
        return formatar_moeda(total, 'R$')
    return str(total)


def diminuir(number=0, porcentagem=0, formatar=False):
    total = number - (number * porcentagem/100)
    if formatar:
        return formatar_moeda(total, 'R$')
    return str(total)
