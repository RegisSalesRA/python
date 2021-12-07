"""
List Comprehension

- Utilizando List comprehension nos podemos gerar novas linhas com dados processados a partir de outro iteravel

# Sintaxxe da list comprehension

[ dado for dado in interavel ]
"""

# Exemplos

numeros = [1,2,3,4,5]

res = [ numero * 10 for numero in numeros]
#
# print(res)

"""
Para entender melhor o que ta acontecendo devemos dividir a expressao em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""

res = [numero/2 for numero in numeros]
# print(res)

#
# def funcao(valor):
#     return valor * valor
#
# res = [funcao(numero) for numero in numeros]
# # print(res)
# #
#
# # List comprehension versos Loop
#
# numeros = [1,2,3,4,5]
#
# numeros_dobrados = []
# for numero in range(1,56):
#     numero_dobrado = numero * 2
#     numeros_dobrados.append(numero_dobrado)
#
# print(numeros_dobrados)
#
# # List Comprehension
# print([numero * 2 for numero in numeros])

# Outros exemplos

# 1

nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2

def nomeMaisculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria','julia', 'pedro','guilherme','vanessa']
print([nomeMaisculo(amigo) for amigo in amigos])


# 3
print([numero * 3 for numero in range(1,10)])

# 4
print([bool(valor) for valor in [0,[], '',True,1,3.14]])

# 5
print([str(numero) for numero in [1,2,3,4,5]])