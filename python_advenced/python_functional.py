# A programação funcional (FP) é um paradigma de programação que trata a computação como uma série de funções matemáticas puras e evita a mutabilidade e o estado compartilhado. 
#E m Python, é possível programar de maneira funcional, embora a linguagem não seja estritamente funcional como Haskell ou Lisp.
# Aqui estão alguns conceitos-chave da programação funcional em Python:

"""
Funções de ordem superior: Python permite que você passe funções como argumentos para outras funções e retorne funções de outras funções. 
Isso é chamado de funções de ordem superior e é um dos pilares da programação funcional.
"""

# Função de ordem superior que recebe uma função como argumento
def aplicar_funcao(func, lista):
    return [func(item) for item in lista]

# Função que será passada como argumento
def dobrar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]
resultado = aplicar_funcao(dobrar, numeros)
print(resultado)  # Saída: [2, 4, 6, 8, 10]

"""
Funções puras: As funções puras são funções que sempre produzem o mesmo resultado para as mesmas entradas e não têm efeitos colaterais.
Em Python, você pode escrever funções puras, embora a linguagem não imponha essa restrição.
"""

# Função pura que não tem efeitos colaterais
def somar(a, b):
    return a + b

# Exemplo de uso
resultado = somar(3, 5)
print(resultado)  # Saída: 8

"""
Imutabilidade: A programação funcional enfatiza a imutabilidade de dados, o que significa que os dados não devem ser alterados após a criação.
Em Python, você pode usar tuplas ou objetos imutáveis, como strings, para alcançar imutabilidade.
"""

# Usando uma tupla para dados imutáveis
ponto = (2, 3)
# ponto[0] = 4  # Isso resultaria em um erro, pois as tuplas são imutáveis

# Usando strings
nome = "Alice"
# nome[0] = "B"  # Isso resultaria em um erro, pois as strings são imutáveis


"""
Compreensões de lista: As compreensões de lista são uma maneira concisa e funcional de criar listas a partir de iteráveis existentes, como listas, tuplas ou sequências.
"""

# Compreensão de lista para criar uma lista dos quadrados de números pares de 0 a 9
quadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(quadrados_pares)  # Saída: [0, 4, 16, 36, 64]
