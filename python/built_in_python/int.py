"""
A função int() em Python é usada para converter um valor em um número inteiro (int). Ela pode converter números inteiros representados como strings, 
números de ponto flutuante ou outras bases numéricas para números inteiros na base 10. Aqui estão alguns exemplos de como usar int():
"""

# Convertendo uma string em um número inteiro
numero_str = "42"
numero_inteiro = int(numero_str)
print(numero_inteiro)  # Saída: 42


# Convertendo um número de ponto flutuante em um número inteiro
numero_float = 3.14
numero_inteiro = int(numero_float)
print(numero_inteiro)  # Saída: 3


# Convertendo uma string que representa um número binário em um número inteiro
numero_binario = "1010"
numero_inteiro = int(numero_binario, 2)
print(numero_inteiro)  # Saída: 10 (em decimal)

