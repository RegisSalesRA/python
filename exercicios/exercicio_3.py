# Dada uma lista de números, encontre o segundo maior número na lista.

lista = list(range(0,40))

lambda_achar_segundo_numero = lambda lista : sorted(lista)[-2]

print(lambda_achar_segundo_numero(lista))