"""
A função type() em Python é usada para determinar o tipo de um objeto. 
Ela aceita um argumento e retorna o tipo desse objeto. O resultado é uma referência à classe do objeto, que pode ser usada para verificar se um objeto é uma instância de uma classe específica.

Aqui estão alguns exemplos de como usar type():
"""

numero = 42
tipo_numero = type(numero)
print(tipo_numero)  # Saída: <class 'int'>


lista = [1, 2, 3, 4, 5]
tipo_lista = type(lista)
print(tipo_lista)  # Saída: <class 'list'>


def minha_funcao():
    pass

tipo_funcao = type(minha_funcao)
print(tipo_funcao)  # Saída: <class 'function'>


class Pessoa:
    pass

pessoa = Pessoa()
tipo_pessoa = type(pessoa)
print(tipo_pessoa)  # Saída: <class '__main__.Pessoa'> (o nome da classe pode variar dependendo do módulo)
