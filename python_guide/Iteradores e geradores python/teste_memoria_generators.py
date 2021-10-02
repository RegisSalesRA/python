"""
Teste de memoria com Generators
"""

def fib_lista(max):
    nums = []
    a,b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste
# for n in fib_lista(100):
#    print(n)

# Funcao usando geradores

def fib_gen(max):
    a,b,contador = 0,1,0
    while contador < max:
        a,b = b, a + b
        yield a
        contador = contador + 1

# Teste 2
for n in fib_gen(100000):
    print(n)