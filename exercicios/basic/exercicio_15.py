# Dada uma lista de palavras, crie uma nova lista que contenha apenas as palavras que são palíndromos (ou seja, que podem ser lidas da mesma forma de trás para frente).


lista = ["Ana" , "Joa", "unther","zum","Bob"]
 

lambda_polindromos = lambda lista : [value for value in lista if value.lower() == value.lower()[::-1]]

print(lambda_polindromos(lista))
