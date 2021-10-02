"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerrow() -> Escreve uma linha


# writer() Gera um objeto para que possamos escrever em um arquivos CSV. utilizando o metodo
# Writerow() para escrever cada linha . Este metodo recebe uma lista
from csv import writer

with open('filmes.csv' 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duracao'])
    while filme != 'Sair':
        filme = input('Informe o nome do filme')
        if filme != 'Sair':
            genero = input('Informe o genero do filme')
            duracao = input('Informe a duracao em minutos')
            escritor_csv.writerow([filme, genero, duracao])

"""

# DictWriter

from csv import DictWriter

with open('filmes.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'Sair':
        genero = input('Informe o numero do filme: ')
        duracao = input('Informe a duracao do filme: ')
        escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
