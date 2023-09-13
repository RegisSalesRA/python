"""
List Comprehension

Nos podemos adicionar estruturas condicionais logicas as nossas List Comprehension
"""
# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 == 1]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par modulo de 2 e 0 e 0 em pyhon e FALSE. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qual quer numero impar  modulo de 2 e 1 , e em python 1 e TRue
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)


