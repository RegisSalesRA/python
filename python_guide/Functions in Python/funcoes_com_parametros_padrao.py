"""
Funcoes  com parametros Padrao ( Default parameters )

- Funcoes onde a passagem de parametro seja opcional;

# EXEmplo de funcao onde a passagem do parametro seja opcional
print('gEek university')

print()

# Exemplo de funcao onde a passagem de paarametro seja obrigatorio
def quadrado(numero):
    return numero ** 2

print(quadrao(3))
print(quadrao()) # Type Error


def exponencial(numero,potencial=2):
    return numero ** potencial

print(exponencial(2,3)) # 2 * 2 * 2
print(exponencial(3,2)) # 3 * 3

print(exponencial(3)) #  Por padrao eleva ao quadrado
print(exponencial(3,5)) #  eleva a potencia informada pelo usuario

# OBS
# Se o usuario passar somente 1 parametro , este sera atribuido ao parametro numero,e sera calculado o quadrado deste numero
# se o usuario passar 2 argumentos , o primeiro  sera atribuido ao parametro numero e o seugndo ao parametro  potencia
# sera calculado a potencia

print(exponencial())

# OBS:  Em funcao Python , os parametros com valores default (padrao) DEVEM sempre estar ao final da declaracao
# ERRO!

def teste(num=2,potencia):
    return num ** potencia

print(teste(6))

# CERTO!

def teste(potencia,num=2):
    return num ** potencia

print(teste(6))


# Outros exemplos

def soma(num1=5,num2=2):
    return num1 + num2

print(soma(4,3))
print(soma(4)) # TypeError
print(soma()) # TypeError


# Exemplo mais complexo

def mostrar_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que voce era o instrutor'
    return f'Ola {nome}'

print(mostrar_informacao())
print(mostrar_informacao(nome='Jose', instrutor=True))
print(mostrar_informacao('Ozzy'))


# Porque utilizar parametros com valor default?

- Nos permite ser mais flexiveis nas funcoes
- Evita erros com parametros incorretos;
- Nos permite trabalhar com exemplos mais legiveis de codigo


# Quais tipos de dados podemos utilizar como valores default para parametros?

- Qual quer tipo de dado:
    - numeros,float,boleanos,funcoes,listas,tuplas,qualquer coisa


# Exemplo Funcao dentro de funcao

def soma(num1,num2):
    return num1,num2

def mat(num1,num2,fun=soma):
    return fun(num1,num2)

def substracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,2, substracao))
# Escopo - Evitar problemas e confusoes...

# Variaveis globais
# Variaveis locais

Instrutor = 'Geek' # Variavel Global

def diz_oi():
    instrutor = 'KeeG'
    return f'Oi {instrutor}'

print(diz_oi())
print(Instrutor)

# OBS : SE tivermos umma variavel local com o mesmo nome de uma variavel global a local tera preferencia

def diz_oi():
    prof = 'Geek' # Variavel Local
    return f'Ola {prof}'

print(diz_oi())
print(prof) #NAmeERROR



# Atencao com variaveis globais (SE PUDER EVITAR? EVITE!!)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError ( Esta sendo utlizada sem ter sido inicializada)
    return total

print(incrementa())

# EXEMPLO 2 COM GLOBAL

total = 0

def incrementa():
    global total

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
"""


# Podemos ter funcoes  que sao declaradas dentro de funcoes , e tambem tem uma forma especial de escopo de variavel
# E uma funcao que passa de local para global
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(dentro()) # Name error
