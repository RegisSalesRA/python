"""

A função str() em Python é usada para converter um objeto em sua representação de string.
 Ela aceita um argumento, que pode ser qualquer objeto Python, e retorna uma representação em string desse objeto. 
 O objetivo principal da função str() é fornecer uma representação legível em texto de um objeto.

Aqui estão alguns exemplos de como usar str():

"""


numero = 42
numero_em_string = str(numero)
print(numero_em_string)  # Saída: "42"


lista = [1, 2, 3, 4, 5]
lista_em_string = str(lista)
print(lista_em_string)  # Saída: "[1, 2, 3, 4, 5]"


dicionario = {"nome": "Alice", "idade": 30}
dicionario_em_string = str(dicionario)
print(dicionario_em_string)  # Saída: "{'nome': 'Alice', 'idade': 30}"


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"

pessoa = Pessoa("Alice", 30)
pessoa_em_string = str(pessoa)
print(pessoa_em_string)  # Saída: "Alice (30 anos)"
