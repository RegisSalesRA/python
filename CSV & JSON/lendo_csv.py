"""
Lendo arquivos CSV

CSV - Comma separeted values - Valores separados por Virgula

# Separador por virgula
1,2,3,4,5,6

"Geek", "university","Python","ciencia","dados"

# Separador por ponto e virgula

1; 2; 3; 4; 5; 6;

"Geek"; "university"; "python;

# Separador por espaco

"geek" "university" "Python"


# E possivel trabalhar mas nao e o ideal

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)

A linguagem python tem duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas:
    - DictReader -> permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

# Reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        # Cada linha e uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centimetros')



# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha e uma lista
        print(f"{linha['None']} nasceu em {linha['Pais']} e mede {linha['Altura']} centimetros")
"""


# DictReader com separador

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha e uma OrderedDict
        print(f"{linha['None']} nasceu em {linha['Pais']} e mede {linha['Altura']} centimetros")