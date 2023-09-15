import os

# caminho_pasta1= r"C:\\Users\\regis.sales\\Desktop\\pasta1\\"   -> use o R caso tente algum problema com as barras
caminho_pasta1= "C:\\Users\\regis.sales\\Desktop\\pasta1\\"
caminho_pasta1 += 'aula116.txt'
# arquivo = open(caminho_pasta1, 'r')
# arquivo.close()

# Usando with nao precisa usar close() ele já fecha automaticamente
with open(caminho_pasta1, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n') 
 

# os.remove(caminho_pasta1)
# os.unlink(caminho_pasta1)
os.rename(caminho_pasta1,'aula_renomeada.txt')