"""
Maps -> Conhecidos em python como dicionarios

Dicionarios em python sao representados por chaves {}

# Iterar sobre dicionarios
for chave in receita:
    print(chave, end=' ')

for chave in receita:
    print(receita[chave], end=' ')

for chave in receita:
    print(f'{chave} : {receita[chave]}', end=' ')


# Acessando as chaves
# Retorna dicionario de chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])


# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

print(receita)


# Desempacotamento de dicionarios

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""

receita = {'jan': 100, 'fev': 250, 'mar': 500}

# Soma*, Valor Maximo* ,Valor Minimo*, Tamanho

# Se os valores forem reais ou inteiros

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))