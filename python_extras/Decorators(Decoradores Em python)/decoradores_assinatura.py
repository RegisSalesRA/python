"""
Decorators com diferentes assinaturas
# Relembrando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar
@gritar
def saudacao(nome):
    return f'ola,eu sou o/a {nome}'
@gritar
def ordenar(principal, acompanhamento):
    return f'ola,eu gostaria de {principal},acompanhando de {acompanhamento},por favor'
# TEstando
# print(saudacao('Angelina'))
print(ordenar('Picanha','Batata frita'))
#Para resolver , utilizamos um padrao de projeto chamado decorator Pattern
# Refatorando com decorator Pattern
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar
@gritar
def saudacao(nome):
    return f'ola eu sou o/a {nome}'
@gritar
def ordenar(principal, acompanhamento):
    return f'ola eu gostaria de {principal}, junto com {acompanhamento}, por favor!'
#print(saudacao('Felicity'))
#print(ordenar('picanha','batata frita'))
@gritar
def lol():
    return 'lol'
print(lol())
# OBS vale apena lembrar que podemos utilizar parametros nomeados
print(ordenar(acompanhamento='Batata frita',principal='Picanha'))
"""


# Decorador por argumento

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)

        return outra

    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando
print(soma_dez(10, 12))  # 22

print(soma_dez(10, 21))  # 22

print(comida_favorita('Pizza', 'churrasco'))
