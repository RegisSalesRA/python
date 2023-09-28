"""

A função bytes() em Python é usada para criar um objeto do tipo bytes a partir de uma sequência de valores inteiros.
Você pode fornecer uma sequência de valores inteiros que representam os bytes que você deseja incluir no objeto bytes.
Aqui está um exemplo:

"""

# Criando um objeto bytes a partir de uma sequência de valores inteiros
bytes_obj = bytes([65, 66, 67, 68])  # Valores inteiros correspondentes a 'ABCD' na tabela ASCII

# Imprimindo o objeto bytes
print(bytes_obj)  # Saída: b'ABCD'

# Acessando os bytes individualmente
print(bytes_obj[0])  # Saída: 65
print(bytes_obj[1])  # Saída: 66
print(bytes_obj[2])  # Saída: 67
print(bytes_obj[3])  # Saída: 68
