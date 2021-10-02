"""
Escopo de variaveis

Dois casos de escopo:

1 - Variaveis globais:
    - Variaveis globais sao reconhecidas , ou seja, seu escopo compreende, todo o o programa.

2 - Variaveis locais:
    - Variaveis locais sao reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    esta limitado ao bloco onde foi declarada

Para declarar variaveis em Python fazemos:

nome_variavel = valor_da_variavel

Python e uma linguagem dinamica de tipagem dinamica, isso significa que
ao declararmos uma variavel, nos nao colocamos o tipo de dado dela.
Este tipo e inferido ao atributo o valor a mesma
"""

numero = 42 # Exemplo de global
print(numero)
print(type(numero))

numero = 'geek'
print(numero)
print(type(numero))

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variavel 'novo esta declarada localmente dentro do bloco do if, portanto e global'
    print(novo)

print(novo)