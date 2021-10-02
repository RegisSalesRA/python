"""
Map

com map, fazemos mapeamento de valores para funcao

import math

def area(r):
    return math.pi * (r ** 2)


raios = [2,5,8,10,44]

# Forma Comum

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2

# Map e uma funcao que recebe dois parametros

areas = map(area,raios)
print(list(areas))

# Forma 3 map com lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
"""

# Para Fixar map

# TEmos dados interaveis

# Dados: a1,a2 ..., an

# Temos uma funcao:

# Funcao : F(x)

# Ultilizamos  a funcao map(f, dados) onde map ira 'mapear' cada elemento dos dados e aplicar a funcao

# O map Object: f(a1), f(a2),f(...),f(an)


listaDados = [1,2,3,4,5]
print(list(map(lambda x: x ** 2,listaDados)))
