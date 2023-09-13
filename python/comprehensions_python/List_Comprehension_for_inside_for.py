"""
List Comprehension For in For

"""


lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

print(lista)


"""

with Comprehension

"""


lista = [
    (x,y,z)
    for x in range(3)
    for y in range(3)
    for z in range(4)
]

print(lista)


"""

with Comprehension loop inside Comprehension

"""

lista  = [[letra for letra in 'Regis'] for x in range(3)]


print(lista)