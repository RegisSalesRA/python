"""
Metodos data e hora

# Com now podemos especificar um timezone (Fuso horario)
agora = datetime.datetime.now()  # Now agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today() # Today hoje
print(hoje)
print(repr(hoje))

# Mudancas ocorrendo a meia-noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# 2020-10-23 00:00:00
# <class 'datetime.datetime'>
# datetime.datetime(2020, 10, 23, 0, 0)


# Encontrar o dia da semana, weekday()

# Os dias da semana metodo weekday() comeca em 0 , sendo a segunda-feira

# 0 monday
# 1 tuesday
# 2 wednesday
# 3 thursday
# 4 friday
# 5 saturday
# 6 sunday

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=3)), datetime.time())
print(manutencao.weekday())


aniversario = input('Qual sua data de nascimento? dd/mm/yyyy: ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Voce nasceu em uma segunda-feira')
elif aniversario.weekday() == 1:
    print('Voce nasceu em uma terca-feira')
elif aniversario.weekday() == 2:
    print('Voce nasceu em uma quarta-feira')
elif aniversario.weekday() == 3:
    print('Voce nasceu em uma quinta-feira')
elif aniversario.weekday() == 4:
    print('Voce nasceu em uma sexta-feira')
elif aniversario.weekday() == 5:
    print('Voce nasceu em uma sabado')
elif aniversario.weekday() == 6:
    print('Voce nasceu em uma domingo')



print(hoje)
#    %Y faz uma diferenca de ano com 2 digitos ou 4 digitos
#    %B te da o nome do mes e o B minusculo as iniciais

hoje_formatado = hoje.strftime('%d/%m/%Y')

print(hoje_formatado)


# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora: minuto


def format_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de marco de {data.year}'
    elif data.month == 2:
        return f'{data.day} de abril de {data.year}'
    elif data.month == 2:
        return f'{data.day} de maio de {data.year}'
    elif data.month == 2:
        return f'{data.day} de junho de {data.year}'
    elif data.month == 2:
        return f'{data.day} de julho de {data.year}'
    elif data.month == 2:
        return f'{data.day} de agosto de {data.year}'
    elif data.month == 2:
        return f'{data.day} de setembro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de outubro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de novembro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de dezembro de {data.year}'


import datetime
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"

hoje = datetime.datetime.today()

print(formata_data(hoje))
"""

import datetime