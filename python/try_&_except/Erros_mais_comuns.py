""""
Erros mais comuns em python
SyntaxError -> Ocorre quando  o python encontra em erro de sintaxe. Ou seja, voce escreveu algo que o
Python nao reconhece com parte da linguagem


Exemplo SyntaxError

a)
def funcao:
    print('Geek University')

b)
def = 1

c)
return


2 - NameError => Ocorre quando uma variavel ou funcao nao foi definida
exemple error

a)
print(geek)

b)
geek()

3 - TypeError -> Ocorre quando uma funcao/operacao/acao e aplicada a um tipo errado
Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

4 - IndexError => ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utiizando
um indice invalido
Exemplo IndexError

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[0][10])

c)
lista = ('Geek',)
print(lista[0][10])

5 - ValueError -> ocorre quando uma funcao/operacao built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado
Exemplos ValueError

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando  tentamos acessar um dicionario com uma chave que nao existe.
Exemplos KeyError

a)
dic = {'python': 'university'}
print(dic['Geek'])

7 - AttributeError -> ocorre quando uma variavel nao tem um atributo/funcao.
Exemplos AttributeError

a)
tupla = (11,2,31,4)
print(tupla.sort())

8 - IdentationError -> Ocorre quando nao respeitam a indentacao do python (4 espacos)
Exemplo Indentation

a)
def nova():
print('Geek')

b)
for i in range(10):
i + i
"""""