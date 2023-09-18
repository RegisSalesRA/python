# Problema dos parâmetros mutáveis em funções Python

"""

Parâmetros mutáveis referem-se a objetos mutáveis que podem ser modificados dentro de uma função e afetar o valor original fora da função.
É importante ter cuidado ao manipular objetos mutáveis passados como argumentos para evitar efeitos colaterais indesejados.

"""

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz', lista=["é o fim"])
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
