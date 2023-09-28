"""

A função frozenset() em Python é usada para criar um objeto de conjunto imutável (frozenset). Um frozenset é semelhante a um conjunto (set), mas é imutável, 
o que significa que seus elementos não podem ser alterados após a criação. Aqui está um exemplo de como usar frozenset()
"""

# Criando um frozenset a partir de uma lista
lista = [1, 2, 3, 4, 5]
fset = frozenset(lista)

# Imprimindo o frozenset
print(fset)  # Saída: frozenset({1, 2, 3, 4, 5})

# Tentando adicionar um elemento ao frozenset (isso resultará em um erro)
try:
    fset.add(6)
except AttributeError as e:
    print("Erro:", e)

