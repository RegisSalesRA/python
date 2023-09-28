"""

A função next() em Python é usada para obter o próximo item de um objeto iterável, como uma lista, 
um iterador personalizado ou um objeto que suporta iteração. Ela permite que você avance para o próximo elemento de um iterável e retorna esse elemento. Se não houver mais elementos no iterável, next() pode aceitar um argumento padrão opcional que será retornado quando o final do iterável for alcançado,
 ou lançar uma exceção StopIteration. Aqui estão alguns exemplos de como usar next():
"""

numeros = [1, 2, 3, 4, 5]
iterador = iter(numeros)

# Obtendo o próximo elemento
prox_elemento = next(iterador)
print("Próximo elemento:", prox_elemento)  # Saída: 1

# Obtendo o próximo elemento novamente
prox_elemento = next(iterador)
print("Próximo elemento:", prox_elemento)  # Saída: 2


numeros = [1, 2, 3]
iterador = iter(numeros)

# Obtendo o próximo elemento
prox_elemento = next(iterador, "Fim da lista")
print("Próximo elemento:", prox_elemento)  # Saída: 1

# Obtendo o próximo elemento
prox_elemento = next(iterador, "Fim da lista")
print("Próximo elemento:", prox_elemento)  # Saída: 2

# Obtendo o próximo elemento após o final da lista
prox_elemento = next(iterador, "Fim da lista")
print("Próximo elemento:", prox_elemento)  # Saída: "Fim da lista"
