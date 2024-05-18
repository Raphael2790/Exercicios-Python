def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")

for nome in ['Maria', 'João', 'Pedro']:
    print(bom_dia(nome))
    print(boa_noite(nome))