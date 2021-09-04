"""
Funcoes com parametro ( de entrada )

- Funcoes que recebem dados para serem processados dentro da mesma;

se a gente pensar em um programa qual quer, geralmente temos:

entrada => processamento => saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:
- Nao possuem entrada:
- Nao possuem saida:
- Possuem entrada mas nao possuem saida
- Nao possuem entrada mas possuem saida
- Possuem entrada e saida

# Refatorando uma funcao

def quadrado(numero):
  #  return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(5))
print(quadrado(2))

ret = quadrado(6)
print(ret)
print(quadrado()) # Print erro TypeError


# Refatorando a funcao

def cantar_parabens(aniversariante):
    print('parabens pra voce')
    print(f'parabens pra {aniversariante}')

cantar_parabens('Marcos')


# Funcoes podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# em uma funcao quantos parametros forem necessarios. Eles sao separados por virgula

# Exemplo

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num, b, msg):
    return (num + b) * msg

print(soma(2 , 5))
print(soma(10 , 2))

print(multiplica(5,2))
print(multiplica(8,2))

print(outra(5,5,'Voce multiplicou '))

# OBS: Se agente informar um numero errado de parametro ou argumentos teremos type error
print(soma(2,3,4)) # TypeError - passando argumentos a mais
print(soma(2)) # TypeError - passando argumentos a menos


# Nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo e {nome} {sobrenome}'

print(nome_completo('Angelina','Jolie'))

# Diferenca entre parametros e argumentos

# Parametros sao variaveis declaradas na definicao de uma funcao
# Argumentos sao dados passados durante a execucao de uma funcao

# A Ordem dos parametros importa!

nome = 'felicity'
sobrenome = 'Jones'
print(nome_completo(sobrenome,nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parametros nos argumentos para informa-los , podemos
# utlizar qualquer ordem.

print(nome_completo(nome='Angelina',sobrenome='Pit'))
print(nome_completo(sobrenome='Pit',nome='Angelina'))


# Erro comum na utilizacao do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1,2,3,4,5,6,7]

print(soma_impares(lista))


# Exemplo normal com if
def par_or_impar(valor):
    if valor % 2 == 0:
        return f'o valor {valor} e um numero par'
    else:
        return f'o valor {valor} e um numero impar'

print(par_or_impar(3))

"""


# Exemplo com listas


def par_or_impar(valores):
    for num in valores:
        print(num)
        if num % 2 == 0:
            print(f'esse numero {num} e par')
        else:
            print(f'Esse numero {num} e um impar')


lista = [1,2, 3, 4, 5, 6]

print(par_or_impar(lista))
