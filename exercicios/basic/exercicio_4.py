# Dada uma lista de números, crie uma nova lista que contenha apenas os números ímpares.

lista = list(range(0,20))

lambda_achar_impares = lambda lista : [value for value in lista if value % 2 == 1]

print(lambda_achar_impares(lista))