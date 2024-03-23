def deve_votar(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


ano = int(input('Em que ano você nasceu? '))
deve_votar(ano)
