"""
A função iter() em Python é usada para criar um objeto iterador a partir de um objeto iterável.
Um iterador é um objeto que pode ser iterado (percorrido) um elemento de cada vez. Você pode usar 
iter() para criar um iterador a partir de objetos como listas, tuplas, strings, dicionários e muito mais. Aqui está um exemplo de como usar iter():
"""

# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]

# Criando um iterador a partir da lista usando iter()
meu_iterador = iter(minha_lista)

# Usando um loop while para percorrer o iterador
while True:
    try:
        elemento = next(meu_iterador)
        print(elemento)
    except StopIteration:
        break

