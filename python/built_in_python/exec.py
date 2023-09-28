"""
A função exec() em Python é usada para executar código Python dinamicamente a partir de uma string.
 Ela permite que você execute blocos de código Python de forma dinâmica. No entanto, é importante usar exec() com cautela,
   pois ele pode executar qualquer código Python e representar um risco de segurança se a entrada não for confiável. Aqui está um exemplo de como usar exec():
"""


# Definindo um bloco de código Python em formato de string
codigo = """
for i in range(5):
    print(f"Valor de i: {i}")
"""

# Usando exec() para executar o código
exec(codigo)
