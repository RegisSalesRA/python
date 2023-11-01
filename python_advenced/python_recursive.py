"""

Recursiva:

A recursão é um método de resolução de problemas. No código, a recursão é implementada usando uma função que chama a si mesma.

O oposto de um algoritmo recursivo seria um algoritmo iterativo. Existe um ramo de estudo que prova que qualquer algoritmo iterativo pode ser escrito recursivamente. 
Enquanto os algoritmos iterativos usam loops for e loops while para simular a repetição, os algoritmos recursivos usam chamadas de função para simular a mesma lógica.

Baseia-se na definição matemática da sequência de Fibonacci, onde F(0) = 0, F(1) = 1 e F(n) = F(n-1) + F(n-2) para n > 1.
Pode ser menos eficiente, especialmente para valores grandes de 'n', 
devido à necessidade de recalculação de valores anteriores várias vezes. Isso leva a um alto consumo de memória e tempo.

"""
OBS:
"""

função fn(eu):
    imprimir (eu)
    fn(eu + 1)
    retornar

fn(1)

No entanto, esse código está realmente errado.
Você vê o problema? As chamadas de função nunca irão parar!
A execução desse código imprimiria números naturais (inteiros positivos) infinitamente (ou até o computador explodir). A returnlinha nunca é alcançada porque fn(i + 1)vem antes dela.

Precisamos do que é chamado de caso base para interromper a recursão. Os casos base são condições no início de funções recursivas que encerram as chamadas.

função fn(eu):
    se eu> 10:
        retornar

    imprimir (eu)
    fn(eu + 1)
    retornar

fn(1)


"""


def fibonacci_recursive(n):
    if n <= 0:
        print(f"primeiro if {n}")
        return 0
    elif n == 1:
        print(f"segundo if {n}")
        return 1
    else:
        print(f"else {n}")
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Exemplo de uso
n = 10  # Altere o valor de 'n' conforme desejado
result = fibonacci_recursive(n)
print(f'O {n}-ésimo número na sequência de Fibonacci (recursivo) é {result}')



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Exemplo de uso:
result = factorial(5)
# print("O fatorial de 5 é", result)
