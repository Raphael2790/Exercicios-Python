from datetime import datetime
from pytz import timezone

# biblioteca para trabalhar com timezones
timezone_sp = timezone('America/Sao_Paulo')
data_aniversario = datetime(1999, 11, 20, tzinfo=timezone_sp)
print(data_aniversario)

data_aniversario = datetime.now(timezone_sp)
print(data_aniversario)
print(data_aniversario.timestamp())
print(datetime.fromtimestamp(1670849077))

data_em_texto = '2024-02-10 08:00:24'
data_format = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_em_texto, data_format)
print(data)
