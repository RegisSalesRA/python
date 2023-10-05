# Dada uma lista de números, crie uma nova lista que contenha apenas os números que são primos

lista = list(range(1,11))


def achar_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

 

print(achar_primo(lista))