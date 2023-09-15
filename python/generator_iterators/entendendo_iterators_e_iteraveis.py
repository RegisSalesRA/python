"""
Entendendo iterators e iterables

Iterator ->  INTERADOR
    - Um objeto que pode ter iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() e chamada:

Iterable ->  INTERAGIVEL
    - Um objeto que ira retornar um iterator quando a funcao iter() for chamada.


nome = 'Geek' # E um Iterable  mas nao e um Iterator .
numeros = [1,2,3,4,5,6] # E um Iterable  mas nao e um Iterator

"""

nome = 'Geek'
numeros = [1,2,3,4,5,6]
 

# print(next(nome)) retorna um erro porque eles nao sao iterator
# print(next(numeros)) retorna um erro porque eles nao sao iterator


# Transformando eles em Iterators para poder interagir neles

itl1 = iter(numeros)
itl2 = iter(nome)

print(next(itl2))

# Ele é um Iterator se conseguir usar o metodo next()




for letra in nome:
    print(f'{letra}', end=' ')
    
# Obs -> Observe que quando ele roda o 'for' ele transforma o nome em iterator fazendo a funcao iter(nome)
