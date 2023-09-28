"""
A função min() em Python é usada para encontrar o valor mínimo em um objeto iterável, como uma lista,
 tupla ou string. Ela retorna o valor mínimo do objeto ou o elemento mínimo com base em alguma ordenação específica,
 dependendo dos argumentos que você passa para ela. Aqui estão alguns exemplos de como usar min():
"""

numeros = [10, 5, 20, 8, 15]
minimo = min(numeros)
print("Valor mínimo:", minimo)  # Saída: 5

texto = "Python"
caractere_minimo = min(texto)
print("Caractere mínimo:", caractere_minimo)  # Saída: 'P'

palavras = ["apple", "banana", "cherry", "date"]
menor_palavra = min(palavras, key=len)
print("Menor palavra (com base no comprimento):", menor_palavra)  # Saída: 'date'
