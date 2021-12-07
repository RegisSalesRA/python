"""
Module Collections - Named Tuple

#Recap Tupla
tupla = (1,2,3)
print(tupla[1])

Named Tuple -> Sao tuplas diferenciadas onde ,especificamos um nome para a mesma e tambem parametro.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parametros

# Forma 1 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', 'idade ,raca, nome')

# Forma 3 - Declaracao Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2,raca='Chow-Chow',nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0]) # Idade
print(ray[1]) # Raca
print(ray[2]) # Nome

# Forma 2

print(ray.idade) # Idade
print(ray.raca) # Raca
print(ray.nome) # Nome

# Qual  o indice desse valor
print(ray.index('Ray'))
# Contar quantas ocorrencias tem nessa tupla
print(ray.count('Ray'))