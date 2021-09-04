"""
Seek and Cursors

seek()


arquivo = open('texto.txt')

print(arquivo.read())


# SEek serve/utilizada para movimentacao do cursor do arquivo
# ela recebe 1 parametro que indica onde queremos colocar o cursor

# movimentacao o cursor pelo arquivo com a funcao seek()
arquivo.seek(0)

print(arquivo.read())


arquivo = open('texto.txt')

# readline() -> Funcao que le o arquivo  linha a linha

ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split())


arquivo = open('texto.txt')
# readlines()

# Separa em linhas
linhas = (arquivo.readlines())

print(len(linhas))


OBS : quando abrimos um arquivo com a funcao open() e criada uma conexao entre o arquivo
no disco do computador e o nosso programa, essa conexao e chamada de streaming. Ao finalizar
os trabalhos com o arquivo devemos fechar essa conexao. Para isso utilizamos a funcao close()

Passos para se trabalhar com um arquivo

1 - Abrir o arquivo
2 - Trabalhar o arquivo
3 - Fechar o arquivo


# 1 - Abrir o arquivo
arquivo = open('texto.txt')
# 2 Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed) # False Verifica se o arquivo esta aberto ou fechado

# 3 Fechar o arquivo:
arquivo.close()

print(arquivo.closed) # True Verifica se o arquivo esta aberto ou fechado

print(arquivo.read())
# SE tentarmos manipular o arquivo apos o seu fechamento , teremos um ValueError


"""


arquivo = open('texto.txt')
# Com a funcao read podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(49))
