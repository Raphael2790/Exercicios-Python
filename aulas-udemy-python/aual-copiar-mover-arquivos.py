import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
PASTA_DESTINO = os.path.join(DESKTOP, 'NOVA_PASTA')

if not os.path.exists(PASTA_ORIGINAL):
    os.makedirs(PASTA_ORIGINAL, exist_ok=True)

if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, PASTA_DESTINO), dir_
        )
        os.makedirs(caminho_diretorio)

    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, PASTA_DESTINO), file_
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

shutil.copytree(PASTA_ORIGINAL, PASTA_DESTINO)
shutil.rmtree(PASTA_DESTINO)
shutil.move(PASTA_ORIGINAL, PASTA_DESTINO + '_EITA')
