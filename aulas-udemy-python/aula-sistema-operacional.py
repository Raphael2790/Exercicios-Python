import os
from itertools import count

counter = count()

os.system('cls')
os.system('echo "Hello World"')

caminho_arquivo = os.path.join('curso', 'video', 'aula', 'aula.txt')
diretorio, arquivo = os.path.split(caminho_arquivo)
nome_arquivo, extensao = os.path.splitext(arquivo)
caminho_existe = os.path.exists(caminho_arquivo)
caminho_deste_arquivo = os.path.abspath('.')
nome_base_path = os.path.basename(caminho_arquivo)

print(caminho_arquivo, diretorio, arquivo, nome_arquivo, extensao, caminho_existe, caminho_deste_arquivo,
      nome_base_path)

caminho_pasta = os.path.join('C:\\User', 'rsssh', 'source', 'repos', 'TorneSeUmProgramador.Apps.Exemplos')

for pasta in os.listdir(caminho_pasta):
    caminho_completo_pasta = os.path.join(caminho_pasta, pasta)
    print(caminho_completo_pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for item in os.listdir(caminho_completo_pasta):
        print(' ', item)


for root, dirs, files in os.walk(caminho_pasta):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'Dir: ', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', the_counter, 'FILE: ', caminho_completo_arquivo)
        # deleta todos os arquivos
        # os.unlink(caminho_completo_arquivo)
        size = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        print(size, stats)

