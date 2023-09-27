"""
A função bool() em Python é usada para converter um valor em seu equivalente booleano (True ou False).
Aqui estão alguns exemplos de como usar bool():
"""

valor = 42
resultado = bool(valor)
print(resultado)  # Saída: True, porque 42 é avaliado como True em contexto booleano

valor_zero = 0
resultado_zero = bool(valor_zero)
print(resultado_zero)  # Saída: False, porque 0 é avaliado como False em contexto booleano



texto = "Olá, mundo!"
resultado_texto = bool(texto)
print(resultado_texto)  # Saída: True, porque a string não está vazia

texto_vazio = ""
resultado_vazio = bool(texto_vazio)
print(resultado_vazio)  # Saída: False, porque a string está vazia


lista = [1, 2, 3]
resultado_lista = bool(lista)
print(resultado_lista)  # Saída: True, porque a lista não está vazia

lista_vazia = []
resultado_lista_vazia = bool(lista_vazia)
print(resultado_lista_vazia)  # Saída: False, porque a lista está vazia


valor_nulo = None
resultado_nulo = bool(valor_nulo)
print(resultado_nulo)  # Saída: False, porque None é avaliado como False



