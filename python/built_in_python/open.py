"""

A função open() em Python é usada para abrir arquivos em diferentes modos de operação,
 permitindo a leitura, escrita ou operações mistas em arquivos de texto ou binários.
 Ela é amplamente usada para lidar com operações de E/S (entrada/saída) de arquivo.
   Aqui estão alguns exemplos de como usar open():
"""


# Abrindo um arquivo chamado "exemplo.txt" em modo de leitura ('r')
arquivo = open("exemplo.txt", "r")

# Lendo o conteúdo do arquivo
conteudo = arquivo.read()
print(conteudo)

# Fechando o arquivo
arquivo.close()



# Abrindo um arquivo chamado "novo_arquivo.txt" em modo de escrita ('w')
arquivo = open("novo_arquivo.txt", "w")

# Escrevendo no arquivo
arquivo.write("Este é um novo arquivo.\n")
arquivo.write("Contendo várias linhas de texto.\n")

# Fechando o arquivo
arquivo.close()
