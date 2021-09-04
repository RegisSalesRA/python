
"""
PRservando metadatas com wraps
Metadatas -> sao dados intricitos em arquivos
wraps -> Sao funcoes que envolvem elementos com diversas finalidades
# Problema
def ver_log(funcao):
    def logar(*args,**kwargs):
        Eu sou uma funcao (logar) dentro de outra
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Voce a dpci,emtacap  {funcao.__doc__}')
        return funcao(*args,**kwargs)
    return logar
@ver_log
def soma(a,b):
        Soma de dois numeros
    return a + b
print(soma(10,30))
print(soma.__name__) # Soma
print(soma.__doc__) # Soma dois numreos

"""

# Resolucao do problema

from functools import wraps


# Problema


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma funcao (logar) dentro de outra"""
        print(f'Voce esta chamando {funcao.__name__}')
        print(f'Voce a dpci,emtacap  {funcao.__doc__}')
        return funcao(*args, **kwargs)

    return logar


@ver_log
def soma(a, b):
    """Soma de dois numeros"""
    return a + b


print(soma(10, 30))
print(soma.__name__)  # Soma
print(soma.__doc__)  # Soma dois numeros
print(help(soma))