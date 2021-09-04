"""
TRabalhando com modulos builtin (Modulos integrados, que ja vem instalados no python)
........................
/Python/Modulos builtin/
````````````````````````
# Utilizando alias (apelido) para modulos/funcoes
import random as rdm

print(rdm.random())

# podemos importar todas as funcoes de um moduloutilizando o *
from random import *

print(random())

# importando todo o modulo
import random
print(random.random())

# utilizando alias (apelidos) para modulos/funcoes

from random import randint as rdi, random as rdm

print(rdi(5,89))
print(rdm())

"""

# Costumamos a utilziar tuple para colocar multiplos imports de um mesmo modulo

from random import (random,randint,shuffle,choice)

print(random())
lista = ['geek','universidade','python']
shuffle(lista)
print(lista)