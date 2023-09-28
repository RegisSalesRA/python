"""
A função max() em Python é usada para encontrar o valor máximo em um objeto iterável,
 como uma lista, tupla ou string. Ela retorna o valor máximo do objeto ou o elemento máximo com base em alguma ordenação específica,
 dependendo dos argumentos que você passa para ela. Aqui estão alguns exemplos de como usar max():
"""

numeros = [10, 5, 20, 8, 15]
maximo = max(numeros)
print("Valor máximo:", maximo)  # Saída: 20


texto = "Python"
caractere_maximo = max(texto)
print("Caractere máximo:", caractere_maximo)  # Saída: 'y'


palavras = ["apple", "banana", "cherry", "date"]
maior_palavra = max(palavras, key=len)
print("Maior palavra (com base no comprimento):", maior_palavra)  # Saída: 'banana'
