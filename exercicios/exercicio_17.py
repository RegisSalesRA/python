# Dada uma lista de números, crie uma nova lista que contenha apenas os números que são maiores do que a média da lista.

lista = list(range(0,20))


lambda_maiores_media = lambda lista : [value for value in lista if value > len(lista) / 2]

print(lambda_maiores_media(lista))