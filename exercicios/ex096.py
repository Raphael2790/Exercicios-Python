print('Controle de terrenos')
print('-'*20)

def culcula_area(alt, comp):
    area = alt * comp
    print(f'A área de um terreno {alt}X{comp} é de {area}m².')


alt = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
culcula_area(alt, comp)
