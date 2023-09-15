# Criando arquivos com python

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir

# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load


# caminho_pasta1= r"C:\\Users\\regis.sales\\Desktop\\pasta1\\"   -> use o R caso tente algum problema com as barras
caminho_pasta1= "C:\\Users\\regis.sales\\Desktop\\pasta1\\"
caminho_pasta1 += 'aula116.txt'
  
# arquivo = open(caminho_pasta1, 'r')
# arquivo.close()

# Usando with nao precisa usar close() ele já fecha automaticamente
with open(caminho_pasta1, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print("#" * 10)

with open(caminho_pasta1, 'r') as arquivo:
    print(arquivo.read())


with open(caminho_pasta1, 'a+') as arquivo:
    arquivo.write("Linha 1")
    arquivo.writelines(("Linha 3\n", 'Linha 4\n'))
    
# Utf-8
with open(caminho_pasta1, 'w', encoding='utf-8') as arquivo:
    arquivo.write("Linha 1")
    arquivo.writelines(("Linha 3\n", 'Linha 4\n'))
