"""

A função reversed() em Python é usada para criar um iterador reverso de um objeto iterável, 
como uma lista, uma tupla ou uma string. Ela retorna um iterador que percorre os elementos do objeto iterável na ordem inversa, 
do último elemento ao primeiro.

Aqui estão alguns exemplos de como usar reversed():

Usando reversed() com uma lista:
"""

lista = [1, 2, 3, 4, 5]
reverso = reversed(lista)

# Iterando pelos elementos na ordem reversa
for elemento in reverso:
    print(elemento)
# Saída:
# 5
# 4
# 3
# 2
# 1


texto = "Python"
reverso = reversed(texto)

# Convertendo o iterador reverso em uma string
string_reversa = ''.join(reverso)
print(string_reversa)  # Saída: "nohtyP"


tupla = (10, 20, 30, 40, 50)
reverso = reversed(tupla)

# Convertendo o iterador reverso em uma lista
lista_reversa = list(reverso)
print(lista_reversa)  # Saída: [50, 40, 30, 20, 10]
