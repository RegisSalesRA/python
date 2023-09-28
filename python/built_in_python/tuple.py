"""
A função tuple() em Python é usada para criar uma tupla a partir de um iterável, 
como uma lista, uma string, ou qualquer outro objeto iterável. Uma tupla é uma coleção imutável de elementos ordenados, e ela é semelhante a uma lista, 
mas com a diferença fundamental de que as tuplas são imutáveis, ou seja, seus elementos não podem ser modificados após a criação.
"""


lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)  # Saída: (1, 2, 3, 4, 5)


texto = "python"
tupla = tuple(texto)
print(tupla)  # Saída: ('p', 'y', 't', 'h', 'o', 'n')


tupla = (10, 20, 30, 40, 50)
print(tupla)  # Saída: (10, 20, 30, 40, 50)


def coordenadas():
    x = 10
    y = 20
    return x, y

coord = coordenadas()
print(coord)  # Saída: (10, 20)

