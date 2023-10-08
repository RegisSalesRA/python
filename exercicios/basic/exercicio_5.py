# Dada uma lista de palavras, encontre a palavra mais longa na lista.

lista = ["Olw", "morningStar" ,"Avenged", "Length","Junnnna"]

def achar_mais_longa(lista):
    pass


lambda_achar_mais_longa = lambda lista : sorted(lista,key=len)[-1]

print(lambda_achar_mais_longa(lista))

