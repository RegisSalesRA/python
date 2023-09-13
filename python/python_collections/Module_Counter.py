"""
Modulo Collections - Counter

collection -> High-performance Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collections Counter que e parecido
com um dicionario , contendo como chave o elemento da lista passada como parametro e como valor a quantidade
da ocorrencia desse elemento

"""

# Utilizando Counter

from collections import Counter

# Podemos utilizar qual quer iteravel, aqui usamos ma lista
lista = [1,1,1,2,2,3,4,5,6,6,6,6,7,7,8,8,8,9,9,0,0,10,10,20,20]

# Utilizando o counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({6: 4, 1: 3, 8: 3, 2: 2, 7: 2, 9: 2, 0: 2, 10: 2, 20: 2, 3: 1, 4: 1, 5: 1})
# Veja que para cada elemento da lista o counter criou uma chave e colocou como valor a quantidade de ocorrencias


# Exemplo 2

print(Counter('Geek University'))
Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


from collections import Counter

# Exemplo 3
Texto = """O azul do escuro das ondas na onda da manha que salvam o dia
 do dia que faz o milagre ja nascido em todos os lugares do mundo"""
print(Counter(Texto))

palavras = Texto.split()

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencia no texto
print(res.most_common(5))

