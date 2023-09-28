"""
A função bytearray() em Python é usada para criar um objeto do tipo bytearray. Assim como o bytes,
 o bytearray permite armazenar uma sequência de valores inteiros que representam bytes.
A diferença principal entre eles é que o bytearray é mutável, ou seja, você pode modificar seus valores após a criação. Aqui está um exemplo:
"""

# Criando um objeto bytearray a partir de uma sequência de valores inteiros
bytearray_obj = bytearray([65, 66, 67, 68])  # Valores inteiros correspondentes a 'ABCD' na tabela ASCII

# Imprimindo o objeto bytearray
print(bytearray_obj)  # Saída: bytearray(b'ABCD')

# Acessando e modificando os bytes individualmente
bytearray_obj[0] = 69  # Modificando o primeiro byte para 'E' (valor inteiro 69)
print(bytearray_obj)  # Saída: bytearray(b'EBCD')

# Adicionando novos bytes ao bytearray
bytearray_obj.extend([70, 71])  # Adicionando 'FG' (valores inteiros 70 e 71) ao final
print(bytearray_obj)  # Saída: bytearray(b'EBCDFG')
