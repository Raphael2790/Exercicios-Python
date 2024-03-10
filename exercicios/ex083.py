expressao = str(input('Digite a expressão: '))
lista_parenteses = list()
expressao_valida = True

for l in expressao:
    if l in '(':
        lista_parenteses.append(l)
    if l in ')':
        if len(lista_parenteses) == 0:
            expressao_valida = False
            break
        lista_parenteses.pop()

if len(lista_parenteses) > 0:
    expressao_valida = False

if expressao_valida:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
