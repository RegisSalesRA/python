"""

A função oct() em Python é usada para converter um número inteiro em sua representação octal (base 8). 
A representação octal usa os dígitos de 0 a 7 e é precedida por "0o" para indicar que é uma representação octal.
 Aqui está um exemplo de como usar oct() para converter um número inteiro em octal:
"""


numero_decimal = 42
numero_octal = oct(numero_decimal)
print("Número octal:", numero_octal)  # Saída: '0o52'


numero_negativo = -18
numero_octal_negativo = oct(numero_negativo)
print("Número octal (negativo):", numero_octal_negativo)  # Saída: '-0o22'
