"""
Leitura de Arquivos

Para o conteudo de um arquivo em Pyhon , utilizamos a funcao integrada open()
que literalmente siginifica `abrir`

open() => Na forma mais simples de utilizacao nos passamos apena um parametro
de entrada, que neste caso E o caminho para o arquivo a ser lido. Essa funcao retorna
um _io.TextIOWrapper e e com ele que trabalhamos entao

# OBS: por padrao , a funcao open() abre o arquivo para leitura. Este arquivo
deve existir , ou entao teremos erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r => modo de leitura r vem de Read significa ler
"""

# Exemplo

arquivo = open('texto.txt')
#print(arquivo)
#print(type(arquivo))

# Para ler o conteudo de um arquivo,apos a sua abertura devemos, utilizar a funcao read()

ret = arquivo.read()
print(type(ret))
print(ret)
print(arquivo.read())

# OBS: o python utiliza um recurso para trabalhar com arquivos chamado cursor, Esse cursor , funciona
# como o cursor quando estamos escrevendo
#
# print(arquivo.read())

# OBS: A funcao read le todo o conteudo dentro do arquivo