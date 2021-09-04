"""
Tipo Float

tipo real,decimal

Casas decimais

OBS: O separados de casas decimais na programacao e o ponto e nao a virgula
"""

# Errado
valor = 1, 44
print(valor)
print(type(valor))

# Certo

valor = 1.44
print(valor)
print(type(valor))

# E possivel fazer dupla atribuicao
valor1 ,valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nos perdemos precisao
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com numeros complexos
variavel = 5j
