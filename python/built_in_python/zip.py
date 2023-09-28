"""
A função zip() em Python é usada para combinar duas ou mais sequências
 (como listas, tuplas ou outros iteráveis) em pares ordenados.
   Ela cria um objeto iterável que produz tuplas contendo elementos correspondentes das sequências de entrada. 
   O comprimento do objeto zip resultante é igual ao comprimento da sequência mais curta de entrada.

Aqui estão alguns exemplos de como usar zip():
"""


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

pares = zip(lista1, lista2)
print(list(pares))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

pares = zip(lista1, lista2)
print(list(pares))  # Saída: [(1, 'a'), (2, 'b'), (3, 'c')]


nomes = ['Alice', 'Bob', 'Carol']
idades = [30, 25, 35]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")


lista1 = [1, 2, 3]
lista2 = ['a', 'b']

pares = zip(lista1, lista2)
print(list(pares))  # Saída: [(1, 'a'), (2, 'b')]
