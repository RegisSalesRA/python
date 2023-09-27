"""
A função any() em Python é uma função integrada que retorna True se pelo menos um dos elementos em um iterável (como uma lista, tupla, conjunto, etc.) for avaliado como True. 
Caso contrário, retorna False. Aqui está um exemplo explicado:
"""


# Exemplo 1: Usando any() com uma lista que contém pelo menos um valor verdadeiro
lista_mista = [False, False, True]
resultado = any(lista_mista)
print(resultado)  # Saída: True

# Exemplo 2: Usando any() com uma lista que contém apenas valores falsos
lista_falsa = [False, False, False]
resultado = any(lista_falsa)
print(resultado)  # Saída: False

# Exemplo 3: Usando any() com uma lista vazia
lista_vazia = []
resultado = any(lista_vazia)
print(resultado)  # Saída: False (uma lista vazia não possui elementos para avaliar)

# Exemplo 4: Usando any() com uma lista de strings
lista_strings = ["", "Python", ""]
resultado = any(lista_strings)
print(resultado)  # Saída: True (pelo menos uma string é avaliada como verdadeira em contexto booleano)

# Exemplo 5: Usando any() com uma lista que contém valores vazios
lista_vazios = [0, "", None, False]
resultado = any(lista_vazios)
print(resultado)  # Saída: False (nenhum valor é avaliado como verdadeiro)


def retornarValor():
    newValue = []
    lista_strings = ["", "Python", ""]
    
    for val in lista_strings:
        if val:
            newValue.append(val)
    return newValue

print("")

print(retornarValor())