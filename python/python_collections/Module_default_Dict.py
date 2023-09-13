"""
Modulo Collections - Default Dict


dicionario = {'curso':'Programacao em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) # Nao existe

Default Dict -> Ao criar um dicionario utilizando-o ,nos informamos um valor default,
podendo utlizar um lambda para isso. Esse valor sera utilizado sempre que nao houver
um valor definido. Caso tentemos acessar uma chave que nao existe , essa chave sera
criada e o valor default sera atribuido

OBS: Lambdas sao funcoes sem nome, que podem ou nao receber um parametro de entrada
e retornar valores.
"""


# Fazendo import
from collections import defaultdict
from collections import Counter

dicionario = defaultdict(lambda : 0)

dicionario['curso'] = 'Programacao Python Essencial'
print(dicionario)

print(dicionario['outro'],) # Keyerror no dicionario comum , mas aqui nao

print(dicionario)
