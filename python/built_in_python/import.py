"""
A função __import__() em Python é uma função embutida que permite importar módulos de forma dinâmica durante a execução de um programa.
 Ela é uma função de baixo nível e raramente é usada em código Python moderno.
 Em vez disso, recomenda-se usar a instrução import padrão para importar módulos.
"""


# Usando __import__() para importar o módulo 'math' dinamicamente
nome_modulo = 'math'
modulo_math = __import__(nome_modulo)

# Acessando funções do módulo 'math'
valor = modulo_math.sqrt(16)
print(valor)  # Saída: 4.0


import math

valor = math.sqrt(16)
print(valor)  # Saída: 4.0

