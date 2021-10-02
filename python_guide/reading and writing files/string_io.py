"""
StringIO

Atencao: para Ler ou escrever dados em arquivos do sistema precisa ter
permissao:
    - Permissao de leitura => para ler o arquivo
    - Permissao de escrita => para escrever o arquivo

StringIO => utilizamos para ler e criar arquivos em memoria
"""

# Primeiro fazemos o import
from io import StringIO

mensagem = 'Este e apeonas um string normal'

# podemos criar um arquivo em memoria ja com uma string inserida ou mesmo vazio para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open('arquivo.txt', 'w')

# agora tendo o arquivo , podemos utilizar tudo que ja sabemos
print(arquivo.read())

# escrevendo outros textos
arquivo.write('outro Texto')

# movimentar o cursor
arquivo.seek(1)

print(arquivo.read())

