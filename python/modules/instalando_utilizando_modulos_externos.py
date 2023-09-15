"""
Modulos Externos

Utilizamos o gerenciador de pacotes python chamado pip - Python installer package

voce pode conhecer todos os pacotes externos oficionais em https://pypi.org

colorama -> E utilizando para permitir impressao de textos coloridos no terminal

instalando com modulo:

pip install nome-do-modulo
"""

from colorama import init,Fore
import pydf

init()
print(Fore.MAGENTA + 'Geek University')




pdf = pydf.generete_pdf('<h1>This is html<h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)


