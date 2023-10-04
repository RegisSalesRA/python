# Dada uma lista de números, encontre o índice do primeiro número ímpar na lista.

lista = list(range(50,100))

def achar_impar_maior(lista):
    indice_impa_value = 0
    for chave,valor in enumerate(lista):
        if valor % 2 == 1:
            indice_impa_value = chave
            break
    return indice_impa_value
 
lambda_achar_impar_maior = lambda lista: next((chave for chave, valor in enumerate(lista) if valor % 2 == 1), None)

print(achar_impar_maior(lista))
print(lambda_achar_impar_maior(lista))