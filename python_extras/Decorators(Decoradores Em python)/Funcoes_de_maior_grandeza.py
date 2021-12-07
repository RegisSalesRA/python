"""
Funcoes de maior grandeza - higher order functions - HOF
O que isso significa??
- Quando uma linguagem de programacao suporte HOF, indica que podemos ter funcoes que retornam
outras funcoes como resultados ou mesmo que podemos passar funcoes como argumentos para outras funcoes, e ate mesmo
criar variavesi de tipos de funcoes nos nossos programas.
OBS: Na sesaco de funcoes nos , utilizamos isso.
Em python, as funcoes sao cidadoes de primeira classe , first class citizen
# Exemplo - Definindo as funcoes
def somar(a, b):
    return a + b
def diminuir(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def calcular(num1, num2, funcao):
    return funcao(num1, num2)
# Testando as funcoes
print(calcular(4, 5, somar))
print(calcular(4, 5, diminuir))
print(calcular(4, 5, multiplicar))
print(calcular(4, 5, dividir))

# Nested functions - funcoes aninhadas

# Em python podemos tambem ter funcoes dentro de funcoes, que sao conhecidas como Nested functions

#cou tambem inner functions(funcoes internas).

# Exemplo
from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Sai daqui ', 'Suma daqui '))
    return humor() + pessoa

# Testando
print(cumprimento('Angelica'))
print(cumprimento('Felicity'))

# Retornando funcoes de outras funcoes
from random import choice
def faz_me_rir():
    def rir():
        return choice(('hahaha', 'jajaja', 'kkkkk'))
    return rir

# Testando
rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funcoes internas/ Nested Functions) podem acessar o escopo de funcoes mais externas.
from random import choice
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha',
                    'kkkk', 'jajajaj'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando
rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
"""
