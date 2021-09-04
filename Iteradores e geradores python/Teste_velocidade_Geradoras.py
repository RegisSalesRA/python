"""
Teste de velocidade com expressoes geradoras


# Generators ( Geradores )

def nums():
    for num in range(1,10):
        yield num

ge1 = nums()
print(ge1) # Generator

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1,10))

print(ge2) # Generation expression

print(next(ge2))
print(next(ge2))
"""

# Realizando o  teste de velocidade
import time

# Generator Expression

get_inicio = time.time()
print(sum(num for num in range(1000000))) # 100 milhoes
get_tempo = time.time() - get_inicio

# List Comprehension

list_inicio = time.time()
print(sum(num for num in range(1000000))) # 100 milhoes
list_tempo = time.time() - list_inicio

print(f'Generator expression levou {get_tempo}')
print(f'List comprehension levou {list_tempo}')

