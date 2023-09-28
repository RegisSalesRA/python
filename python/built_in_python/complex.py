"""
A função complex() em Python é usada para criar um número complexo a partir de números reais.
Um número complexo é uma combinação de uma parte real e uma parte imaginária, onde a parte imaginária é representada com o sufixo "j".
Aqui está um exemplo de como usar complex():
"""

# Criando números complexos
numero_complexo_1 = complex(2, 3)  # 2 + 3j
numero_complexo_2 = complex(4.5, -1.2)  # 4.5 - 1.2j

# Imprimindo os números complexos
print("Número complexo 1:", numero_complexo_1)
print("Número complexo 2:", numero_complexo_2)

# Realizando operações com números complexos
soma = numero_complexo_1 + numero_complexo_2
produto = numero_complexo_1 * numero_complexo_2

print("Soma dos números complexos:", soma)
print("Produto dos números complexos:", produto)
