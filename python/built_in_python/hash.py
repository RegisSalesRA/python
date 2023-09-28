"""
A função hash() em Python é usada para calcular o valor hash de um objeto.
 O valor hash é um número inteiro que representa de forma única o conteúdo do objeto. Os objetos que são iguais (de acordo com o método __eq__)
 devem ter o mesmo valor hash. No entanto, nem todos os objetos em Python são hashable. 
Tipos mutáveis, como listas e dicionários, não podem ser usados como chaves em dicionários ou elementos em conjuntos, pois não são hashable.
"""

numero = 42
valor_hash = hash(numero)
print("Valor hash do número:", valor_hash)


texto = "Python"
valor_hash = hash(texto)
print("Valor hash da string:", valor_hash)


tupla = (1, 2, 3)
valor_hash = hash(tupla)
print("Valor hash da tupla:", valor_hash)


lista = [1, 2, 3]
try:
    valor_hash = hash(lista)
except TypeError as e:
    print("Erro:", e)


