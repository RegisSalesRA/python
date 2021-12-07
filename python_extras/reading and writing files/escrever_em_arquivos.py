"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura nao podemos realizar a escrita nele apenas ler
da mesma forma se abrirmos um arquivos para escrita nao podemos ler, somente escrever nele.

# Ao abrir um arquivo para escrita , o arquivo e criado no sistema operacional

PAra escrevermos dados em um arquivo , apos abrir o arquivo utlizamos a funcao write().
Esta funcao recebe uma string como parametro, caso contrario teremos typerror

Abrindo um arquivo para escrita com o modo `w` ,  se o  arquivo nao existir sera criado
caso ele ja exista, o anterior sera apagado e um novo sera criado. Dessa forma, todo
o conteudo no arquivo anterior e perdido

# Exemplo de escrita
# Passando 'w' do ingles escrita se fosse 'r' seria leitura do ingles read
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados de arquivos e bastante facil\n')
    arquivo.write('Podemos colocar quantas linhas quisermos\n')
    arquivo.write('Outros')
    arquivo.write('1')


# Forma nao pythonica
arquivo = open('mais.txt', 'w')

arquivo.write('Texto qual quer\n')
arquivo.write('Texto qual quer 2\n')

arquivo.close()


with open('geek.txt', 'w') as arquivo:
    arquivo.write('geek ' * 1000)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informa a fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + ' ')
        else:
            break