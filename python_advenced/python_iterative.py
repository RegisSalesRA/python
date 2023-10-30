"""

Iterativa:

A abordagem iterativa utiliza um loop para calcular os números da sequência de Fibonacci.
Começa com os dois primeiros números (0 e 1) e, em seguida, calcula os números subsequentes somando os dois últimos.
Armazena os valores já calculados em uma lista (ou variáveis) para evitar recálculos.
É mais eficiente em termos de uso de recursos e tempo, especialmente para números grandes, pois não recalcula os mesmos valores várias vezes.

"""


def fibonacci_iterative(n):
    fib = [0, 1]
    while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])
    return fib[n]

# Exemplo de uso
n = 10  # Altere o valor de 'n' conforme desejado
result = fibonacci_iterative(n)
print(f'O {n}-ésimo número na sequência de Fibonacci (iterativo) é {result}')
