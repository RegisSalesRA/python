"""
Modulo random o que sao modulos??

- Em python , modulos nada mais sao  que outros arquivos python.

Modulo Random -> Possui varias funcoes para geracao de numeros pseudo-aleatorio


# OBS: existem duas formas de se utilizar um modulo ou funcao deste

# Forma 1 - importanndo todo o modulo

import random

# random() -> Gera um numero pseudo-aleatorio entre 0 e 1

# Ao relizar o import de
# todo modulo todas as funcoes,atributos,classes e propriedade que estiverem dentro do modulo ficaram disponivels
# Ficarao em memoria

# Deste modulo , entao esta nao seria a forma ideal de utilizacao, nos veremos uma forma melhor na forma 2

print(random.random())

# Nao confunda a funcao random() com o pacote random. Pode parecer confuso,mas a funcao random() e apenas uma
# funcao dentro do modulo random.


# Forma 2 - importantando uma funcao especifica do modulo

from random import random

# No import acima,estamos falando: Do modulo random, importa a funcao random

for i in range(10):
    print(random())



# uniform() ->  Gerar um numero pseudo-aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3,7)) #  nao e incluido


# randint() -> gera valores pseudo-aleatorios entre os valores estabelecidos
from random import randint

# Gerador de apostas para mega-sena
for i in range(6):
    print(randint(1,6), end=' ') # Comeca em 1 e vai ate 60


# Choices() -> Mostra um valor aleatorio entre um iteravel
from random import choice
jogadas = ['pedra','papel','tesoura']

print(choice(jogadas))


from random import shuffle
# shuffle() -> Tem a funcao de embaralhar dados
cartas = ['k','b','c','a']
print(cartas)
shuffle(cartas)
print(cartas)
"""

