# Dada uma lista de números, remova todos os números pares da lista.


lista = list(range(60,112))


lambda_removendo_pares = lambda lista : [value for value in lista if value % 2 == 1]

print(lambda_removendo_pares(lista=lista))