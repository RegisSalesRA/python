"""
A função ord() em Python é usada para obter o valor inteiro (representação numérica) do código Unicode de um caractere.
 Ela retorna o valor Unicode do caractere especificado como argumento. Aqui está um exemplo de como usar ord():
"""


caractere = 'A'
valor_unicode = ord(caractere)
print(f"O valor Unicode de '{caractere}' é {valor_unicode}")  # Saída: O valor Unicode de 'A' é 65


caractere_especial = '€'
valor_unicode_especial = ord(caractere_especial)
print(f"O valor Unicode de '{caractere_especial}' é {valor_unicode_especial}")  # Saída: O valor Unicode de '€' é 8364

caractere_acentuado = 'á'
valor_unicode_acentuado = ord(caractere_acentuado)
print(f"O valor Unicode de '{caractere_acentuado}' é {valor_unicode_acentuado}")  # Saída: O valor Unicode de 'á' é 225


