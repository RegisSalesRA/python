"""
A função vars() em Python é usada para retornar o dicionário de atributos de um objeto,
 incluindo atributos especiais como __dict__, que contém os atributos de instância do objeto. 
 A função vars() aceita um argumento, que deve ser um objeto, e retorna um dicionário contendo os atributos desse objeto.

Aqui estão alguns exemplos de como usar vars():
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)

atributos = vars(pessoa)
print(atributos)  # Saída: {'nome': 'Alice', 'idade': 30}


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)

# Modificando o atributo 'idade' usando vars()
atributos = vars(pessoa)
atributos['idade'] = 31

print(pessoa.idade)  # Saída: 31


# Em um arquivo chamado "meu_modulo.py"
var1 = 10
var2 = "Python"

# Em outro arquivo Python
import meu_modulo

atributos_do_modulo = vars(meu_modulo)
print(atributos_do_modulo)  # Saída: {'var1': 10, 'var2': 'Python'}
