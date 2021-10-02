"""
Sistema de arquivos e navegacao

PAra fazer uso de manipulacao de arquivos do sistema operacional , precisamos imporrtar
e fazer uso do moduo os.

os -> Operating system - sistema operacional

# Fazer o import
import os

# getcwd() diretorio current work directory - diretorio de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# Para mudar o diretorio, podemos utilizar chdir()
os.chdir('..')
print(os.getcwd())


# Fazer import
import os

# Podemos checar se um diretoorio e absoluto ou relativo
# isabs funcao diretorio absoluto
print(os.path.isabs('/home/geek'))


# Fazer import
import os

#OBS para usuarios windows
# se voce,infelizmente,estiver utilizando um computador com windows
# tera que ter cuidado ao verificar diretorios

print(os.path.isabs('C:\\Users\\geek'))


# Fazer import
import os

# podemos ter mais detalhes no sistema operacional
print(os.uname())
# podemos identificar o sistema operacional com o mdulo os
print(os.name) # posix (linux, mac), nt (Windows)


# Fazer import
import sys
# Verificando a plataforma
print(sys.platform)


import os
# Veja que o os.path.join() recebe dois parametros ,sendo o primeiro o diretorio atual e o segundo o
# diretorio que se juntando ao atual

# podemos listar  os arquivos e diretorios com o listdir()
print(len(os.listdir()))
"""

import os

# podemos listar  os arquivos e diretorios com mais detalhes com scandir()


scanner = os.scandir()

arquivos = list(os.scandir())
print(arquivos)
print(arquivos)

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # e um diretorio? False
print(arquivos[0].is_file())  # e um arquivo? True
print(arquivos[0].is_symlink())  # E um link simbolico? False
print(arquivos[0].name)  # nome do arquivo
print(arquivos[0].path)  # caminho ate o arquivo
print(arquivos[0].stat())  # ??

# OBS: quando utilizamos a funcao scandir() nos precisamos fecha-la, assim abrimos um arquivo

scanner.close()