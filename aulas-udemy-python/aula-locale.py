import locale
from calendar import calendar

# seta a localização do programa para a mesma do sistema
locale.setlocale(locale.LC_ALL, '')

# seta a localizacao para português
# o sistema operacional deve suportar a localização especificada
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(calendar(2023))
