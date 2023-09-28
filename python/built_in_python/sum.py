"""

A função sum() em Python é usada para calcular a soma dos elementos de um iterável,
 como uma lista, uma tupla ou um conjunto. Ela aceita um iterável como argumento e, opcionalmente,
   um valor inicial (padrão é 0). A função sum() retorna a soma de todos os elementos do iterável mais o valor inicial, se fornecido.

Aqui estão alguns exemplos de como usar sum():
"""

lista = [1, 2, 3, 4, 5]
soma = sum(lista)
print(soma)  # Saída: 15


tupla = (10, 20, 30, 40, 50)
soma = sum(tupla)
print(soma)  # Saída: 150


conjunto = {2, 4, 6, 8, 10}
soma = sum(conjunto)
print(soma)  # Saída: 30


lista = [1, 2, 3, 4, 5]
valor_inicial = 10
soma_com_inicial = sum(lista, valor_inicial)
print(soma_com_inicial)  # Saída: 25 (10 + 1 + 2 + 3 + 4 + 5)
