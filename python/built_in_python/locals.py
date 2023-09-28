"""
A função locals() em Python retorna um dicionário que representa as variáveis locais no escopo atual.
 Esse dicionário mapeia nomes de variáveis locais para seus valores correspondentes. 
Ela é frequentemente usada para inspecionar as variáveis locais dentro de uma função ou método. Aqui está um exemplo de como usar locals():
"""

def minha_funcao():
    variavel_local = 42
    nome = "Alice"
    
    # Obtendo as variáveis locais usando locals()
    variaveis_locais = locals()
    
    # Exibindo as variáveis locais
    for nome_variavel, valor_variavel in variaveis_locais.items():
        print(f"{nome_variavel}: {valor_variavel}")

minha_funcao()
