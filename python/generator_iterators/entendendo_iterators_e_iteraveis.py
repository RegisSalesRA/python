"""
Entendendo iterators e iterables

Iterator ->
    - Um objeto que pode ter iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() e chamada:

Iterable ->
    - Um objeto que ira retornar um iterator quando a funcao iter() for chamada.


nome = 'Geek' # E um iterable mas nao e um iterator
numeros = [1,2,3,4,5,6] # E um iterable mas nao e um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))

"""

nome = 'Geek'

for letra in nome:
    print(f'{letra}', end=' ')