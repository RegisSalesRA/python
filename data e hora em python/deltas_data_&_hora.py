"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:50:30.999999
data_final = dd/mm/yyyy 15:50:30.999999

delta = data_final - data_inicial

# Temos data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2020, 10, 28, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento.days)

"""

import datetime


data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=15)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)