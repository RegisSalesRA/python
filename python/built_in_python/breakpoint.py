"""
A função breakpoint() em Python é usada para inserir um ponto de interrupção em seu código,
permitindo que você inicie um depurador interativo (como o PDB - Python Debugger) naquele ponto.
Isso pode ser útil para inspecionar variáveis, executar comandos e depurar problemas em seu código.

Aqui está um exemplo de como usar breakpoint():

"""

def calcular_valor(x, y):
    resultado = x + y
    breakpoint()  # Inserir ponto de interrupção
    return resultado

a = 5
b = 7
soma = calcular_valor(a, b)

print("Resultado da soma:", soma)
