# Crie uma lista de números e ordene-a em ordem decrescente.

lista = list(range(20,50))


lambda_ordernar_descrscente = lambda list : sorted(lista,reverse=True)

print(lambda_ordernar_descrscente(lista))