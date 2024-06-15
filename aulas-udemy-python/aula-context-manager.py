from contextlib import contextmanager
from typing import TextIO
import os

file_name = 'aula.text'

# aciona o recurso com o acionamento do metodo exit() ao final da execução
# similar ao using do dotnet
# opções de abertura arquivos: 'r'(leitura), 'w'(escrita), 'a'(append), 'w+/r+'(leitura e escrita)
with open(file_name, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Alguma coisa escrita\n')
    arquivo.writelines(
        ('Linha 2 \n', 'Linha 3 \n')
    )
    # volta o cursor de leitura para o ponto (seek)
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    print(arquivo.readlines())


def read_file_stream(file_path: str) -> str:
    with open(file_path, 'r') as file:
        for line_file in file:
            yield line_file.strip()


for line in read_file_stream(file_name):
    print(line)

generator = (linha.strip() for linha in open(file_name, 'r'))

for linha in generator:
    print(linha)


# decorator para permitir execução da função com with
@contextmanager
def open_file(file_path_context: str) -> TextIO:
    file_context = open(file_path_context, 'r')
    try:
        yield file_context
    finally:
        file_context.close()


# Uso do context manager com generator expression
with open_file(file_name) as file:
    generator = (line.strip() for line in file)
    for line in generator:
        print(line)

# renomeia ou move o arquivo
os.rename(file_name, 'aula-exemplo.txt')
# apaga o arquivo, também possivel com remove
os.unlink(file_name)
