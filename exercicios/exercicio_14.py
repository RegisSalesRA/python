# Dada uma lista de números, encontre o terceiro número ímpar na lista.

lista = list((range(0,56)))
 
lambda_achar_numero = lambda lista: list(set([value for value in lista if value  % 2 == 1]))[2]

print(lambda_achar_numero(lista))