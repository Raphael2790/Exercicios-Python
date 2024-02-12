# Representação de cores \033[style;text;backgroundm
# Códigos estilo 0,1,4,7
# Códigos cores 30~37
# Códigos background 40~47
# Exemplos \033[0:30:41m, \033[4:33:44m

print('\033[1;31;43mOlá, Mundo!\033[m')

a= 2
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
