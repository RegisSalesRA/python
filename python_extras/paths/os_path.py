import os

caminho = os.path.join("home","Desktop", "curso",'arquivo.txt')

print(caminho)

diretorio,arquivo = os.path.split(caminho)


""" Pegar a extensao
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo,extensao_arquivo)
"""


print(os.path.exists(caminho))
print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.dirname(caminho))

new_path = r'C:\\Users\\regis.sales\\Desktop\\django_images'

caminho_new = os.path.join("")
for pasta in os.listdir(caminho_new):
    caminho_completo = os.path.join(caminho,pasta)
    
    if not os.path.isdir(pasta):
        continue
    
    for imagem in os.listdir(caminho_completo):
        print(imagem)