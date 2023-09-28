"""

A função enumerate() em Python é usada para iterar sobre uma sequência (como uma lista, tupla ou string)
 juntamente com um contador que rastreia o índice ou a posição do item atual na sequência.
   A função retorna um objeto enumerador que gera tuplas contendo o índice e o valor do item na sequência. Aqui está um exemplo de como usar enumerate():
"""

# Definindo uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]

# Usando enumerate() para iterar sobre a lista com um contador
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")


