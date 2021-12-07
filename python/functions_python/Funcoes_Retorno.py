"""
Funcoes com retorno

numeros = [1,2,3]

ret_pop = numeros.pop()

print(f'retorno de pop: {ret_pop}')

ret_pr = print((numeros))

print(f' Retorno de print: {ret_pr}')

OBS: Em python, Quando uma funcao nao retorna nenhum valor , o retorno e None
OBS: Funcoes python que retornam valores devem retoranar esses valores com a palavra reservada "RETURN"

OBS: Nao precisamos necessariamente criar uma variavel para receber o retorno
de uma funcao . Podemos passar  a execuao da funcao para outras funcoes

# Vamos refatorar esta funcao para que ela retorno o valor

def quadrado_de_7():
    return 7 * 7

# Criamos uma variavel para receber o valor da funcao
ret = quadrado_de_7()

print(f'Retorno {ret}')
print(f'Retorno {quadrado_de_7() + 1}')


# Refatorando a primeira funcao

def diz_oi():
    return 'Oi!'

print(diz_oi())

alguem = 'Pedro'

diz_oi()
print(alguem)

# OBS sobre a palavra reservada return
# 1 - ela finaliza a funcao ,ou seja,ela sai da execucao da funcao
# 2 - Podemos ter , em uma funcao, diferenca returns;
# 3 - podemos ,em uma funcao ,retornar  qual quer tipo de dado e ate mesmo multiplos valores


# Exemplo 1

def diz_oi():
    print('Estou antes executado apos o retorno')
    return 'Oi!'
    print('Estou sendo executado apos o retorno')

print(diz_oi())


# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'
print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5,


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(outra_funcao())
print(type(outra_funcao()))


# Vamos criar uma funcao para jogar a moeda

from random import random

def jogar_moeada():
    # Gera um numero pseudo-randomico entre 0 e 1

    if random() > 0.5:
        return 'Cara'
    else:
        return 'Coroa'
print(jogar_moeada())
"""


# Erros comuns na utlizacao do retorno, que na verdade nem e erro, mas sim codificacao desnecessaria

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False
print(eh_impar())