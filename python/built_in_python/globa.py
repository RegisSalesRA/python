"""
A função globals() em Python é usada para obter um dicionário que representa o escopo global atual, que contém todas as variáveis globais do programa.
 O dicionário mapeia nomes de variáveis globais para seus valores. Aqui está um exemplo de como usar globals():
"""

# Variável global
nome_global = "Alice"

# Função que acessa a variável global usando globals()
def mostrar_nome_global():
    variaveis_globais = globals()
    nome = variaveis_globais["nome_global"]
    print("Nome global:", nome)

# Chamando a função
mostrar_nome_global()
