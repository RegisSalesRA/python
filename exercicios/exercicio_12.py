# Dada uma lista de palavras, crie uma nova lista que contenha apenas as palavras que contêm a letra "e".


lista = ["Ana", "Anel","Juan","elegivel","Satisfatorio"]


lambda_conte_e = lambda lista: [value for value in lista if "e" in value]

print(lambda_conte_e(lista))
