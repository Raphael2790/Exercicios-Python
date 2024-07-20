from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_inicio_em_texto = '2024-02-10 08:00:24'
data_fim_em_texto = '2024-02-20 08:20:24'
data_format = '%Y-%m-%d %H:%M:%S'

data_inicio = datetime.strptime(data_inicio_em_texto, data_format)
data_fim = datetime.strptime(data_fim_em_texto, data_format)

delta = data_fim - data_inicio
print(delta)
time_delta = timedelta(minutes=10)
nova_data = data_inicio + time_delta
print(nova_data)

# pacote python-dateutil
# mostra de forma mais compreensiva a diferen;a entre data
# possui maior flexibilidade na manipula;áo de datas
delta_util = relativedelta(data_fim, data_inicio)
print(delta_util)
