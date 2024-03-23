def escreva(texto, separator='~', espaco_extra=2):
    tamanho_texto = len(texto)
    espaco_total = tamanho_texto + espaco_extra
    print(f'{separator}'*espaco_total)
    print(f'{texto:^{espaco_total}}')
    print(f'{separator}'*espaco_total)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube', '=')
escreva('CeV', '=', 10)
