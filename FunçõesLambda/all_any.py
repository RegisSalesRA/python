# All retorna true se todos os elementos de interavel sao verdadeiros ou ainda se o iteravel esta vazio

nomes = ['Carlos','Caio','Cabral','Crota','Cleopatra','trunks']

# print(all(nome[0] == 'C' for nome in nomes))

# print(all([letra for letra in 'eiof' if letra if 'aeiouf']))

# print(all([num for num in [4,2,6,8,10] if num % 2 == 0]))

# Any() => Retorna true se qualquer elemento do iteravel for verdadeiro. se0 o iteravel estiver vazio, retorna False

# print(any([0,2,4,6])) # True
#
# print(any([0,False, {},[]])) # False
#
# print(any([nomes[0] == 'C' for nome in nomes]))

print(any([num for num in [4,2,10,6,8] if num %2 ==0]))