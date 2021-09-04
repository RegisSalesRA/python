"""
Modulo collections: Ordered Dict


# em um dicionario , a ordem de insercao dos elementos nao e garantida.
dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5}

for chave , valor in dicionario.items():
    print(f'chave={chave} : valor={valor} ')

OrderedDict -> E um dicionario , que nos garante a ordem de insercao dos elementos.


# FAzendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,})
print(dicionario)
"""

from collections import OrderedDict
# Entendendo a diferenca entre Dict e Ordered Dict

# Dicionarios comuns

dict1 = {'a':1,'b':2}
dict2 = {'b':2,'a':1}

print(dict1 == dict2) # True -> Ja que a ordem dos elementos nao importa para o dicionario

# Ordered Dict

odict1 = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5,})
odict2 = OrderedDict({'a':2,'b':1,'c':3,'d':4,'e':5,})

print(odict1 == odict2) # False -> JA que a ordem dos elementos importa para o OrderedDict