"""
Sistema de arquivos - Manipulacao

import os
# descobrindo se um arquivo ou diretorio existe

# Arquivo
print(os.path.exists('arquivos.txt')) # False
print(os.path.exists('frutas.txt')) # True

import os
# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


import os
# criando arquivos

os.mkdir('arquivo-teste4.txt')

os.mknod('home/geek/')

# Se voce estiver utilizando no mac os, pode ja ver um erro permissionerror

import os
os.mkdir('templates')

# OBS: a funcao mkdir() cria um diretorio se este nao existir. caso exista, teremos FileExistsError


import os
# Renomear arquivos e diretorios

os.rename('templates','geek')

# OBs se o diteorio nao existir teremos um filenotfoundError

# OBS se o diretorio que queremos renomar nao estiver vazio, teremos OSError

# Arquivos
os.rename()

import os
# ATENCAO ! Tome muito cuidado com os comandos de deletacao, ao deletarmos um arquivo ou diretorio, eles
# nao vao para a lixeira. Eles somem.

os.remove('geek.txt')

# OBS: se voce estiver no windows e o arquivo que voce for deletar estiver em uso voce tera um erro

# OBS: caso o arquivo nao exista, teremos o FilenotfoundError

# OBS: se voce informar um diretorio ao inves de um arquivo, teremos IsAdiretory


# Removendo uma arvore de diretorios

for arquivo in os.scandir('geek'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if arquivo.is_file():
        os.rmdir(arquivo.path)
"""

