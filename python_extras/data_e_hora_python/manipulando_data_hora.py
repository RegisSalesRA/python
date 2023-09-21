
""" 
Manipulando Data e Hora

Python tem um modulo built-in (integrado) para se trabalhar com data e hora
chamado datetime
"""


import datetime

# print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# REtorna a data e hora corrente
print(datetime.datetime.now())  # 2020-10-22 19:15:43.224347  BR 22/10/2020

# Datetime.datetime(year,mounh,day,hour,minute,second,microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()
print(inicio)

# alterar o horario para 16h, 0 min,0 segundo, 0 microsegundo
inicio = inicio.replace(hour=16,minute=0,second=0,microsecond=0)
print(inicio)


evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

aniversario = input('Informa sua data de nascimento  (dd/mm/yyyy): ')

# Criando um array separando os elementos pela barra
aniversario = aniversario.split('/')

aniversario = datetime.datetime(int(aniversario[2]), int(aniversario[1]), int(aniversario[0]))
print(aniversario)
print(type(aniversario))
 

import datetime

evento = datetime.datetime.now()

# Acessando individual dos elementos de data e hora

print(evento.year) # ano
print(evento.month) # mes
print(evento.day) # dia
print(evento.hour) # hora
print(evento.minute) # minuto
print(evento.microsecond) #microsegundos

print(dir(evento))