
# Dada uma lista de números, crie uma nova lista que contenha apenas os números que são múltiplos de 3.


lista = list(range(0,56))

lambda_multioplo_3 = lambda lista: [value for value in lista if value % 3 == 0]

print(lambda_multioplo_3(lista))
