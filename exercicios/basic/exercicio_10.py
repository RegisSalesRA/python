# Crie duas listas de números e calcule a soma dos elementos correspondentes das duas listas.


lista_1 = list(range(0,12))
lista_2 = list(range(15,34))

lambda_elementos_somar_listas = lambda lista,lista2: [sum(lista)+ sum(lista2)]

print(lambda_elementos_somar_listas(lista=lista_1,lista2=lista_2))