"""
Modos de abertura de arquivo

r => abre modo leitura - padrao
w => abre modo escrita - sobrescreve caso o arquiv ja exista
x => abre para escrita somente se o arquivo nao existir
a =>

try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo 2.\n')
except FileExistsError:
    print('Arquivo ja existe')

# Exemplo a
with open('frutas.txt') as arquivo:
    while True:
        fruta = input('Informe a fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + ' ')
        else:
            break

"""


with open('outro.txt','r+') as arquivo:
    arquivo.write('Adicionar')
    arquivo.seek(11)
    arquivo.write('Nova linha')
    arquivo.seek(5)
    arquivo.write('Mais uma linha')