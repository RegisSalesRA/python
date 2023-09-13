"""
**kwargs

Esse e so mais um parametro,mas diferente do args que coloca valores extras
em uma tupla, o kwargs exige que utiliamos parametros nomeados, e transforma esses
parametros extras em um dicionario


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} e {cor}')

cores_favoritas(marcos='verde', kulia='azul', julia='amarelo', vanessa='branco')

# OBS: Os parametros args e kwargs nao sao obrigatorios

cores_favoritas()
cores_favoritas(geek='Geek')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['Geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pythonico'
    elif 'Geek' in kwargs:
        return f"{kwargs['Geek']} Geek!"
    return 'Nao tenho certeza de quem voce E'

print(cumprimento_especial())
print(cumprimento_especial(Geek='Python'))
print(cumprimento_especial(Geek='Oi'))
print(cumprimento_especial(Geek='Especial'))

# Nas nossas funcoes, podemos ter (NESTA ORDEM):
- Parametros obrigatorios
- *args:
- PArametros default ( nao obrigatorios)
- **kwargs


def minha_funcao(idade,nome,*args,solteiro=False,**kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8,'Julia')
minha_funcao(18,'Felicity',4,5,6,solteiro=True)
minha_funcao(34,'Felipe',eu='Nao',voce='Vai')
minha_funcao(20,'Carla',9,2,3,java=False,python=True)


# Entenda porque e importante manter a ordem dos parametros na declaracao

#Funcao com a ordem correta de parametros
#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Funcao com a ordem incorreta de parametros
def mostra_info(a, b,instrutor='Geek',*args,  **kwargs):
    return [a, b, args, instrutor, kwargs]


a=1
b=2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome':'university','cargo':'Instrutor'}


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))


# Desempacotar  com *kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome':'Felicity', 'sobrenome':'Jones'}

print(mostra_nomes(**nomes))
"""


def soma_multiplos_numeros(a,b,c,**kwargs):
    print(a +b +c)

lista = [1,2,3]
tupla = (1,2,3)
conjunto = {1,2,3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1,b=2,c=3)

soma_multiplos_numeros(**dicionario)

# OBS Os nomes da chave em um dicionarios devem ser os mesmos dos parametros da funcao

#dicionario = dict(d=1,e=2,f=3) # TypeError
#soma_multiplos_numeros(**dicionario)


dicionario = dict(a=1,b=2,c=3, nome='Geek')

soma_multiplos_numeros(**dicionario,lang='Python')



def mostro_argumentos_nomeados(*args,**kwargs):
    print("Nao nomeados", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(2,3,nome="Regis", sobrenome="Sales")



configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)