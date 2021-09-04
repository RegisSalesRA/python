"""
Modulo Collections - Deque

Podemos dizer que o deque e uma lista de alta performance
"""

# Importar

from collections import deque

# Criando deque

deq = deque('geek')

print(deq)

# Adicionando elementos no deque

deq.append('y') # Adiciona no final

print(deq)

deq.appendleft('k') # Adiciona no comeco

print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o ultimo elemento

print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento

print(deq)