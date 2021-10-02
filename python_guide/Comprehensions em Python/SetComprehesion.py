"""
Set comprehension

Lista = [1,2,3,4,5]
Set = {1,2,3,4,5}
"""

# Exemplos

numeros = {num for num in range(1,7)}
print(numeros)

# Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)

# OBS: Faca uma alteracao na estrutura acima para gerar um dicionario ao inves e set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Para finalizar
letras = {letra for letra in 'Geek University'}
print(letras)