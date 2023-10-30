"""

Recursiva:

A abordagem recursiva utiliza a recursão, ou seja, uma função chama a si mesma para calcular os números da sequência.
Baseia-se na definição matemática da sequência de Fibonacci, onde F(0) = 0, F(1) = 1 e F(n) = F(n-1) + F(n-2) para n > 1.
Pode ser menos eficiente, especialmente para valores grandes de 'n', 
devido à necessidade de recalculação de valores anteriores várias vezes. Isso leva a um alto consumo de memória e tempo.

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
