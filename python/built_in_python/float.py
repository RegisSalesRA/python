"""
A função float() em Python é usada para criar um número de ponto flutuante (número real) 
a partir de um valor numérico ou de uma string que represente um número real. 
Aqui estão alguns exemplos de como usar float():
"""

valor_inteiro = 42
valor_float = float(valor_inteiro)
print(valor_float)  # Saída: 42.0

string_numero = "3.14"
numero_float = float(string_numero)
print(numero_float)  # Saída: 3.14

string_numero_inteiro = "100"
numero_float = float(string_numero_inteiro)
print(numero_float)  # Saída: 100.0

string_notacao_cientifica = "1.23e-4"
numero_float = float(string_notacao_cientifica)
print(numero_float)  # Saída: 0.000123
