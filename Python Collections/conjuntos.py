"""
Conjuntos

- Conjuntos em qual quer linguagem de programacao estamos fazendo referencia a teoria dos conjuntos da matematica

- aqui no python , os conjuntos sao chamados de Sets

dito isto, da mesma forma que na matematica:

- Sets (conjuntos) nao possuem valores duplicados:
- Sets (conjuntos) nao possuem valores ordenados:
- Elementos nao sao acessados via indice,ou seja,conjuntos nao sao indexados;

Conjuntos sao bons para se utlizar quando precisamos armazenar elementos mas nao nos importamos com a ordenacao deles
quando nao precisamos se preocupar com chaves valores e itens duplicados

Os conjuntos (sets) sao referenciados em python com chaves {}

Diferenca entre conjuntos (Set) e mapas (dicionarios) em python:
    - Um dicionario tem chave/valor:
    - Um conjunto tem apenas valor:


# Definindo um conjunto

# Forma 1
s = set({1,2,3,4,5,5,5,6,6,1,11,22,33,6,}) # Repare aqui que temos valores repetidos.
print(s)
print(type(s))

# OBS: ao criar um conjunto , caso seja adicionado um valor ja existente , o mesmo
# sera ignorado sem gerar error e nao fara parte do conjunto

# Forma 2 - Mais comum

s = {1,2,3,4,5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto

if 3 in s:
    print('tem o 3')
else:
    print('nao tem o 3')


# Importante lembrar que, alem de nao termos valores duplicados, nao temos ordem

# Listas aceitam valores duplicados, entao temos 9 elementos
lista = [99,2,2,34,23,21,1,44,5]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, entao temos 9 elementos
tupla = (99,2,2,34,23,21,1,44,5)
print(f'tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios nao aceitam valores duplicados, entao temos 8 elementos
dicionario = {}.fromkeys([99,2,2,34,23,21,1,44,5],'dict')
print(f'dicionario:{dicionario} com {len(dicionario)} elementos')

# Conjuntos nao aceitam valores duplicados, entao temos 8 elementos
conjunto = {99,2,2,34,23,21,1,44,5}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')


# Assim como todo outro conjunto python podemos colocar todos os tipos de dados misturados em series

s = {1, 'b',True,33.2,44}
print(s)
print(type(s))

# podemos iterar em um set normalmente
for valor in s:
    print(valor)


# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes informaram
# Informam manualmente a cidade de onde vieram

# Nos adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
# e ter repeticao

cidades = ['Belo horizonte','sao paulo','campo grande','sao paulo','cuiaba']

print(len(cidades))

# Agora precisamos saber quantas cidades distintas , ou seja, unicas, temos.

# O que voce faria?

# Podemos utlizar o Set para isso

# Set vai remover duplicidade
print(len(set(cidades)))

# adicionando elementos em um conjunot

s = {1,2,3}
s.add(4) # Duplicidade nao da erro, mas e simplismente ignorado
print(s)

# Remover elementos em um conjunto
s = {1,2,3}
print(s)

# Forma 1

# Nao e indice e um valor! informaos o valor a ser removido
# Conjuntos nao sao indexados
ret = s.remove(3)
print(ret)

# OBS: caso o valor nao seja encontrado sera gerado o error KeyError, nenhum valor e retornado

# Forma 2

s.discard(2)
print(s)

# OBS: Se o valor nao for encontrado nenhum erro e gerado!


s = {1,2,3}
print(s)

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

novo =s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy

novo = s
print(novo)

novo.add(4)

print(novo)
print(s)



s = {1,2,3}

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)



# Metodos matematicos de conjuntos

# imagine que temos dois conjuntos: um contendo estudantes do curso python e um
# contendo estudantes do curso de jave

estudantes_python = {'marcos','fernando','jejum','jacu'}
estudantes_java = {'fernando','gustavo','paula'}

# Veja que alguns alunos que estudam python tambem estdam Java.
# precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - utilizamos union

union1 = estudantes_java.union(estudantes_python)
print(union1)

# Forma 2 - utilizando o caractere pipe |

unico2 = estudantes_java | estudantes_python
print(unico2)

# Gerar um conjunto de estudantes que estao em ambos os cursos

# Forma 1 - utilizamos intersection

ambos1 = estudantes_java.intersection(estudantes_python)

# Forma 2 - utilziando o &

ambos2 = estudantes_java & estudantes_python
print(ambos2)


# Gerar um conjunto de estudantes que nao estao no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
"""
