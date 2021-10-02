"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimoso arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with e utilizado para criar um contexto de trabalho onde os recursos
utilizados sao fechados apos o bloco with.

"""

# o block - Forma pythonica de manipular arquivos

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

# print(arquivo.read())
print(arquivo.closed)