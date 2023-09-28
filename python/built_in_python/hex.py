"""
A função help() em Python é usada para obter informações de ajuda interativa sobre objetos, módulos, funções, métodos, classes, e muito mais. 
Ela fornece uma descrição e documentação sobre o objeto ou tópico solicitado. A função help() pode ser usada de várias maneiras:
"""

# Obtendo ajuda sobre a função built-in 'len'
help(len)

# Obtendo ajuda sobre o módulo 'math'
import math
help(math)


# Criando uma lista
lista = [1, 2, 3]

# Obtendo ajuda sobre o método 'append' da lista
help(lista.append)

# Obtendo ajuda sobre a função built-in 'print'
help(print)

# Definindo uma classe simples
class MinhaClasse:
    """Esta é a documentação da classe MinhaClasse."""

    def __init__(self):
        """Este é o construtor da classe."""
        pass

# Obtendo ajuda sobre a classe MinhaClasse
help(MinhaClasse)

