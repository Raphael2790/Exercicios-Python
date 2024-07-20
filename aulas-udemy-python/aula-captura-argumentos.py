import sys
from argparse import ArgumentParser

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print("Voce não informou argumentos")
else:
    try:
        print(f'Voce passou os argumentos {argumentos[1:]}')
    except IndexError:
        print('Faltam argumentos')

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    # type=str, # Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', # Valor padrão
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+', # Recebe mais de um valor
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
    print(args.basic)
else:
    print('O valor de basic:', args.basic)

print(args.verbose)
