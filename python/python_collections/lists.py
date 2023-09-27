"""
Listas em python funcionam como vetores/matrizes em outras linguagens , com a diferenca
de serem dinamicos e tambem de poderemos colocar QUALQUER tipo de dado

- Dinamico: Nao possui tamanho fixo; Ou seja , podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: Nao possuem tipo de dado fixo; Ou seja, podemos colocar qual quer tipo de dado;

As listas de python sao representadas por: []

"""

type([])

lista1 = [1, 99, 2, 5, 6,1,42,3,3,1,2,3,1,4,5,6,6,2,3434,242,342,343,4]

lista2 = ['G', 'd', 'H', 'z', 'S', 'q', 'p']

lista3 = []

lista4 = list(range(11))

# Criando so elementos em uma lista
lista5 = list('Geek university')

# Podemos facilmente checar se determinado valor esta contido na lista
# num = 2
# if num in lista4:
#     print(f'Encontrei o numero {num}')
# else:
#     print(f'Nao encontrei o numero {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
#print(lista1)

# Podemos facilmente contar o numero de ocorrencias de um valor em uma lista
# print(lista1.count(1))
# print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas,utilizamos a funcao append

OBS: Com o append nos conseguimos adicionar somente um elemento por vez
"""

#print(lista1)
#lista1.append(500)
#print(lista1)

lista1.append([501,502,503]) # Coloca a lista como elemento unico (sublista)
#print(lista1)

if [501,502,503] in lista1:
    print('Encontrei a lista')
else:
    print('Nao encontrei a lista')

lista1.extend([123,44,67]) # coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posicao do indice
# OBS: Isso nao substitui o valor inicial o mesmo sera alocado para direita na lista
lista1.insert(2, 'Novo valor')
print(lista1)

lista6 = lista1 + lista2
# Lista.extends(lista2)
print(lista6)


# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])


# Copiar uma lista

lista6 = lista2.copy()
print(lista6)
print(lista2)

# Contar quantos elementos existe em uma lista!? Usando o len
# Usando o len e pratico
print(len(lista1))

#Podemos remover facilmente o ultimo elemento de uma lista
# OBS: O pop nao somente remove o ultimo elemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

#Podemos remover um elemento pelo indice
# Os elementos a direita deste indice serao deslocados para a esquerda
# Se nao houver elemento no indice informado, teremos um erro IndexError
lista5.pop(2)
print(lista5)


# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista
nova = [1,2,3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'programacao em python: Essencial'
#print(curso)
curso = curso.split()
#print(curso)

# OBS: Por padrao, o split separa os elementos da lista pelo espaco entre elas

# Exemplo 2
curso2 = 'progrmacao,em,python,essencial'
print(curso2)
curso2 = curso2.split(',')
print(curso2)


# Convertendo uma lista em uma string
lista6 = ['Programacao','em','Python','Essencial']
print(lista6)

# OBS : Abaixo estamos falando: Pega a lista6,coloca espaco entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# OBS : Abaixo estamos falando: Pega a lista6,coloca cifrao entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)



# Podemos realmente colocar qual quer tipo de dado dentro de uma lista
lista6 = [True,1,1.23,'Geek','d',[1,2,3],12412412]
print(lista6)
print(type(lista6))

# Iterando sobre lista

# Exemplo 1 - utilizando o for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - utilizando o while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adiciona um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)



# Utilizando variaveis em listas
numero = [1,2,3,5,6]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

num = [num1,num2,num3,num4,num5]

print(numero)
print(num)

# Fazemos acesso aos elementos de forma indexada

cores = ['verde','amarelo','azul','branco']
print(cores[2])

# Fazer acesso aos elementos de forma indexada inversa
# PAra entender melhor pense indice negativo,pense na lista como um circulo,onde
# o final de um elemento esta ligado ao inicio da lista
print(cores[-1]) # branco


for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for coloca a chave no indice e o valor em cor
for indice, cor in enumerate(cores):
    print(indice,cor)


# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
print(lista)


# Outros metodos nao tao importantes mas tambem uteis
# Encontrar o indice de um elemento na lista

# Em qual index da lista esta o valor 6?
numeros = [5,6,5,7,8,9,10]
#print(numeros.index(6))

# OBS: caso nao tenha esse elemento da lista sera apresentado erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, qual indice comecar  a buscar
print(numeros.index(5,1)) # buscando a partir do indice 1
print(numeros.index(5,2)) # buscando a partir do indice 2

# Podemos fazer busca dentro de um range, indice/fim
print(numeros.index(8,3,6)) # Buscar o indice do valor 8, entre os indices 6 a 8


# Revisao de slicing
# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com parametro 'inicio'


list1 = [8, 0, 9, 5]

# Positivas:
print(list1[::1])   # Todos os elementos em ordem original: [8, 0, 9, 5]
print(list1[::2])   # Todos os elementos em passos de 2: [8, 9]
print(list1[1::2])  # A partir do segundo elemento, em passos de 2: [0, 5]
print(list1[1:])    # Do segundo elemento até o final: [0, 9, 5]
print(list1[:3])    # Do início até o quarto elemento (não inclusivo): [8, 0, 9]
print(list1[1:3])   # Do segundo ao terceiro elemento (não inclusivo): [0, 9]
print(list1[1:4])   # Do segundo ao quarto elemento (não inclusivo): [0, 9, 5]

# Negativas:
print(list1[::-1])  # Todos os elementos em ordem reversa: [5, 9, 0, 8]
print(list1[::-2])  # Todos os elementos em ordem reversa em passos de 2: [5, 0]
print(list1[1::-1]) # Do segundo elemento até o início em ordem reversa: [0, 8]
print(list1[:-1])   # Todos os elementos exceto o último: [8, 0, 9]
print(list1[-3:])   # Os últimos três elementos: [0, 9, 5]
print(list1[-2:-1]) # Do penúltimo ao último elemento (não inclusivo): [9]


# Invertendo valores em uma lista

nomes = ['Geek','University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)


# Soma,procurar valor maximo/minimo, tamanho

# Se os valores forem inteiros ou reais.

lista = [1,2,3,4,5]

print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista


# Transformar em tupla
lista = [1,2,3,4]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotamento de lista

lista = [1,2,3]

num1,num2,num3 = lista

print(num1)
print(num2)
print(num3)

"""
OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados,teremos ValueError
"""


# Copiando lista para outra (shallow copy deep copy)

lista = [1,2,3]
print(lista)
nova = lista.copy()

print(nova)

nova.append(4)
print(lista)
print(nova)

# Veja que ao utlizar lista.copy copiamos os dados da lista para uma nova lista mas elas ficaram totalmente independentes
# ou seja modificando uma lista nao afeta a outra
# Isso em python e chamado de deep copy

# Forma 2 - Shallow copy

lista = [1,2,3 , [5,4]]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a copia via atribuicao e copiamos os dados da lista para a nova lista
# Mas ao modificar um dos elementos da lista  essa modificao refletiu em ambas as listas
# Isso em python e shallo copy

# Forma 3 Deep copy

import copy

d1 = {
    'c1':1,
    'c2':2,
    'l1':[0,1,2]
}

d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)

"""
type([])

lista1 = [1, 99, 2, 5, 6, 1, 42, 3, 3, 1, 2, 3, 1, 4, 5, 6, 6, 2, 3434, 242, 342, 343, 4]

lista2 = ['G', 'd', 'H', 'z', 'S', 'q', 'p']

lista3 = []

lista4 = list(range(11))

# Criando so elementos em uma lista
lista5 = list('Geek university')

cores = ['branco','azul','verde','amarelo']
"""
