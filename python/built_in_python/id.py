"""
A função id() em Python é usada para obter o identificador único (ID) de um objeto.
 O ID é um número inteiro que representa exclusivamente o objeto durante o tempo de vida do programa.
 Cada objeto em Python possui um ID único. Aqui está um exemplo de como usar id():
"""

# Criando uma lista
lista = [1, 2, 3]

# Obtendo o ID da lista
id_da_lista = id(lista)

# Imprimindo o ID da lista
print("ID da lista:", id_da_lista)
