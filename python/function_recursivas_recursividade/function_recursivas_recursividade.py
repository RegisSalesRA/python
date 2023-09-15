# Function recursivas


"""
Toda funcao revursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recurisvo que resolve o pequeno problema
- Um caso base que para a recursão
- fatorial - n! = 5! = 5 * 4 *3 * 2 * 1 = 120
"""

def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())