"""

A função range() em Python é usada para criar um objeto de sequência que representa uma sequência de números inteiros.
 Essa sequência é frequentemente usada em loops for para iterar sobre um intervalo específico de valores. A função range() pode aceitar um,
   dois ou três argumentos e retorna um objeto range com os números especificados.

Aqui estão alguns exemplos de como usar range():
"""


# Cria um objeto range que representa valores de 0 a 9 (0 a 9 - 1)
intervalo = range(10)

# Usando um loop for para iterar sobre os valores
for numero in intervalo:
    print(numero)


# Cria um objeto range que representa valores de 5 a 9 (5 a 9 - 1)
intervalo = range(5, 10)

# Usando um loop for para iterar sobre os valores
for numero in intervalo:
    print(numero)


intervalo = range(5, 10)
lista_de_valores = list(intervalo)
print(lista_de_valores)  # Saída: [5, 6, 7, 8, 9]
