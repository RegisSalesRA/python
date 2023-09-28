"""

A função set() em Python é usada para criar um objeto conjunto (set),
 que é uma coleção de elementos únicos e não ordenados.
   Os elementos em um conjunto não têm uma ordem específica e são armazenados de forma desordenada. 
   Além disso, um conjunto não permite elementos duplicados, garantindo que cada elemento seja único dentro do conjunto.

Aqui estão alguns exemplos de como usar set() para criar conjuntos:
"""

conjunto_vazio = set()
print(conjunto_vazio)  # Saída: set()


lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4, 5}


conjunto = set([1, 2, 3, 4, 5])
print(conjunto)  # Saída: {1, 2, 3, 4, 5}


texto = "abracadabra"
conjunto = set(texto)
print(conjunto)  # Saída: {'a', 'b', 'r', 'c', 'd'}

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
uniao = conjunto_a.union(conjunto_b)
print(uniao)  # Saída: {1, 2, 3, 4, 5}

# Interseção
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)  # Saída: {3}

# Diferença
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)  # Saída: {1, 2}

# Teste de associação
pertence = 2 in conjunto_a
print(pertence)  # Saída: True

