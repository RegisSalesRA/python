# Dada uma lista de números, crie uma nova lista que contenha apenas os números que são múltiplos de 2 ou 3.


lista = list(range(1,20))


lambda_achar_multiplo_2_3 = lambda lista : [value for value in lista if value % 2 == 0 and value % 3 == 0]

print(lambda_achar_multiplo_2_3(lista))