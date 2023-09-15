"""
Ultilizando lambdas

Conhecidas como expressoes Lambdas, ou simplismente lambdas, sao funçoes sem nome, ou seja,
funçoes anonimas

EX basico

"""

def funcao(x):
    return 3 + x * 2

print(funcao(2))

funcao = lambda x: 3 + x * 2

print(funcao(3))


# Expressos lambdas com multiplas entradas

nome_completo = lambda nome,sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' erica','  julia  '))

# Em funcoes  python podemos ter nenhuma ou varias entradas. Em lambdas tambem

amo = lambda: 'Eu amo python'
uma = lambda x: x ** 2
duas = lambda x, y: x + y
tres = lambda x, y, z: x + y + z

# n = lambda x1,x2, ..., xn: <expressoes>

print(amo())
print(uma(2))
print(duas(2,3))
print(tres(2,3,4))

#outro exemplo

autores = ['Isan stream','tien aukti','tim drake','drake burton','josh drown','frank la frank','frank.tucharc','NomeSObreno endende','h.c tolkein']
# print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
