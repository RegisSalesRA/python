"""
A função all() em Python é uma função integrada que retorna True se todos os elementos em um iterável (como uma lista, tupla, conjunto, etc.)
forem avaliados como True. Caso contrário, retorna False. Aqui está um exemplo explicado:
"""

# Exemplo 1: Usando all() com uma lista de valores verdadeiros
lista_verdadeira = [True, True, True]
resultado = all(lista_verdadeira)
print(resultado)  # Saída: True

# Exemplo 2: Usando all() com uma lista que contém pelo menos um valor falso
lista_mista = [True, True, False]
resultado = all(lista_mista)
print(resultado)  # Saída: False

# Exemplo 3: Usando all() com uma lista vazia
lista_vazia = []
resultado = all(lista_vazia)
print(resultado)  # Saída: True (uma lista vazia é considerada como "todos verdadeiros" porque não há elementos para avaliar)

# Exemplo 4: Usando all() com uma lista de strings
lista_strings = ["Python", "é", "uma", "linguagem"]
resultado = all(lista_strings)
print(resultado)  # Saída: True (todas as strings são consideradas "verdadeiras" em contexto booleano)

# Exemplo 5: Usando all() com uma lista que contém valores vazios
lista_vazios = [0, "", None, False]
resultado = all(lista_vazios)
print(resultado)  # Saída: False (pelo menos um valor é avaliado como False)


def retornarValor():
    newValue = []
    lista_vazios = [0, "oi", None, False]
    
    for val in lista_vazios:
        if val:
            newValue.append(val)
    return newValue

print("")

print(retornarValor())