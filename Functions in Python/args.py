"""
Entendendo o *args

- O *args e um parametro , como outro qual quer, isso significa  que voce podera
chamar de qualquer coisa, desde que comece com asterisco

Exemplo:

*xix

Mas por convencao, utilizamos o nome *args para difinilo

Mas o que e o *args?

o parametro *args utilizado em uma funcao, coloca os valores extras informados como
entrada en uma tupla. entao desde ja lembre-se que tuplas sao imutaveis

# Exemplo

def soma_todos_numeros(num1,num2,num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4,6,9))

# print(soma_todos_numeros(4,6,9)) # Type Error
#print(soma_todos_numeros(1,2,3,4)) # Type Error



# Entendo o args

# Exemplo 1
# def soma_todos_numeros(*args):
#     total = 0
#     for numero in args:
#         total = total + numero
#     return total

# Exemplo 2

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(1,2))
print(soma_todos_numeros(1,2,3,4))
print(soma_todos_numeros(3,2,2,2,2,2))

# Outro exemplo de utilizacao do args

def verficia_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    else:
        return 'Eu nao tneho certezaa quem e voce...!'


print(verficia_info())
print(verficia_info(1, True, 'University', 'Geek'))
print(verficia_info(1, 'University', 3.23))

"""


def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3,4,5,6))

numeros = [1, 2, 3, 4, 5,6,7]

# Desempacotamento

print(soma_todos_numeros(*numeros))

# OBS o * serve para que informemos ao python que estamos passando como argumento uma colecao de dados
# Ele sabera que precisara antes de desempacotar esses dados