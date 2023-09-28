"""
A função memoryview() em Python é usada para criar um objeto de memória que permite visualizar e manipular a representação em bytes de um objeto mutável,
 como uma sequência (string, bytes, bytearray) ou um array.
 O memoryview fornece uma interface de visualização de memória eficiente para acessar os bytes subjacentes do objeto sem copiá-los. 
Isso pode ser útil ao trabalhar com grandes volumes de dados binários, como arquivos ou buffers de rede.
"""

# Criando um objeto de bytes
dados = b"Hello, World!"

# Criando um memoryview a partir do objeto de bytes
view = memoryview(dados)

# Acessando os bytes subjacentes
primeiro_byte = view[0]
print("Primeiro byte:", primeiro_byte)  # Saída: 72 (código ASCII para 'H')

# Modificando um byte
view[0] = 74  # Alterando 'H' para 'J'
print("Dados após a modificação:", dados)  # Saída: b'Jello, World!'

