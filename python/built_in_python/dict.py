"""
A função dict() em Python é usada para criar um novo dicionário (um tipo de estrutura de dados) ou para converter outros tipos de sequências em dicionários.
 Aqui estão alguns exemplos de como usar dict():
"""


dicionario_vazio = dict()
print(dicionario_vazio)  # Saída: {}

dicionario = dict({"nome": "Alice", "idade": 30})
print(dicionario)  # Saída: {'nome': 'Alice', 'idade': 30}

dicionario = dict(nome="Bob", idade=25)
print(dicionario)  # Saída: {'nome': 'Bob', 'idade': 25}

lista_de_tuplas = [("chave1", "valor1"), ("chave2", "valor2")]
dicionario = dict(lista_de_tuplas)
print(dicionario)  # Saída: {'chave1': 'valor1', 'chave2': 'valor2'}

chaves = ["a", "b", "c"]
valores = [1, 2, 3]
dicionario = dict(zip(chaves, valores))
print(dicionario)  # Saída: {'a': 1, 'b': 2, 'c': 3}

chaves = ["x", "y", "z"]
valores = [10, 20, 30]
dicionario = {chave: valor for chave, valor in zip(chaves, valores)}
print(dicionario)  # Saída: {'x': 10, 'y': 20, 'z': 30}

