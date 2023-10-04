# Dada uma lista de palavras, crie uma nova lista que contenha o comprimento de cada palavra.

lista = ["Palav" ,"Ola", "Jaaaaaan", "Mikasa", "eren"]

lambda_comprimento_palavra = lambda lista: [len(value) for value in lista]

print(lambda_comprimento_palavra(lista))