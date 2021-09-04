"""
Tuplas

Tuplas sao bastantes parecidas com listas

Existem basicamente duas diferencas basicas:

1 - As tuplas sao representadas por parenteses()

2 - As tuplas sao imutaveis: Isso significa que ao se criar uma tupla ela nao muda. Toda
operacao em uma tupla gera uma nova tupla


# CUIDADO 1: As tuplas sao representadas por (), mas veja:

tupla = (1,2,3,4,5,6)
#print(tupla)
#print(type(tupla))

tupla2 = 1,2,3,4,5,6
#print(tupla2)
#print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4)
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# Conclusao: podemos concluir que tuplas sao definidas por virgula e nao pelo uso do paranteses

(4) -> Nao e tupla
(4,) -> e tupla
4, -> e tupla


# Podemos gerar uma tupla dinamicamente com range( inicio,fim,passo )
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University','Programacao em python: Essencial')
escola , curso = tupla

print(escola)
print(curso)

# OBS: Colocar um numero diferente para desempacotar vai da erro

# MEtodos para adicao e remocao de elementos nas tuplas nao existem,dado o fato das tuplas serem imutaveis


# Soma*, Valor maximo, Valor minimo e tamanho

# Se os valores forem todos inteiros ou reais

tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenacao de tuplas
tupla1 = (1,2,3)
print(tupla1)
tupla2 = (4,5,6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# Sobrescrevendo o metodo dela
# Tuplas sao imutaveis mas podemos sobrescrever os seus valores
tupla1 = tupla1 + tupla2

# Verificar se determinado elemento esta contido na tupla

tupla = (1,2,3)
print(33 in tupla)


# Interando sobre uma tupla
tupla = (1,2,3)
for n in tupla:
    print(n)

for indice,n in enumerate(tupla):
    print(indice,n)

# Contando elementos dentro de ua tupla

tupla = ('a','b','c','d','a','z','p')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola.count('G'))


# Dicas na utilizacao de tuplas

# Devemos utilizar tuplas SEMPRE que nao precisamos modificar os dados contidos em uma colecao

# Exemplo 1

meses = ('Janeiro','fevereiro','marco','abril')

# meses = ['Janeiro','fevereiro','marco','abril']

print(meses)

# O acesso a elementos de uma tupla tambem e semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qal indice o elemento esta na tupla

meses = ('Janeiro','fevereiro','marco','abril')
print(meses.index('Janeiro'))

# OBS: Caso  elemento nao existe , sera gerado Value error


# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9])
"""

# porque utilizar tuplas?

# - tuplas sao mais rapidas que listas
# - tuplas deixam seu codigo mais seguro

# - Isso porque trabalhar com elementos imutaveis traz seguranca para o codigo

# copiando uma tupla para outra
tupla = (1,2,3)
print(tupla)
nova = tupla
print(nova)
print(tupla)

outra = (4,5,6)
nova = nova + outra

print(nova)
print(tupla)