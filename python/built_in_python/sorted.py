"""

A função sorted() em Python é usada para ordenar uma sequência iterável, como uma lista, uma tupla ou uma string,
 e retorna uma nova lista contendo os elementos ordenados. Ela aceita um iterável como argumento e, opcionalmente,
 permite especificar argumentos adicionais para controlar a ordenação, como a chave de ordenação e a ordem reversa.

Aqui estão alguns exemplos de como usar sorted():


"""

numeros = [4, 1, 7, 2, 5]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 2, 4, 5, 7]


palavras = ["banana", "abacaxi", "laranja", "maçã"]
palavras_ordenadas = sorted(palavras)
print(palavras_ordenadas)  # Saída: ['abacaxi', 'banana', 'laranja', 'maçã']


texto = "python"
texto_ordenado = sorted(texto)
print(''.join(texto_ordenado))  # Saída: "hnopty"


palavras = ["banana", "abacaxi", "laranja", "maçã"]
palavras_ordenadas_por_tamanho = sorted(palavras, key=len)
print(palavras_ordenadas_por_tamanho)  # Saída: ['maçã', 'banana', 'laranja', 'abacaxi']


numeros = [4, 1, 7, 2, 5]
numeros_ordenados_reverso = sorted(numeros, reverse=True)
print(numeros_ordenados_reverso)  # Saída: [7, 5, 4, 2, 1]
