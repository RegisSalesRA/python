"""
Assertions ( checagem/Questionamento )

Em python utilizamos a palavra reservada `assert` para realizar simples
afirmacoes utilizadas nos testes.

utilizamos o 'assert' em uma expressao que queremos checar se e valida ou nao
Se a expressao for verdadeira , retorna None e caso seja falsa levanta um erro

# OBS: Nos podemos especificar ,opcionalmente, um segundo argumento ou mesmo uma mensagem
de error personalizada

# OBS: A palavra 'assert' pode ser utilizada em qual quer funcao ou codigo nosso...
nao precisa ser exclusivamente nos tesstes

Se o programa Python for executado com o parametro -O nenhum assert
sera valido, ou seja todas as suas validacoes ja eram
"""

def soma_numeros_positivos(a,b):
    assert a > 0 and b > 0, 'Ambos numeros precisam ser positivos'
    return a + b

#ret = soma_numeros_positivos(-2,4)
#print(ret)

def comer_fast_food(comida):
    assert comida in ['pizza','sorverte','doces','batata frita','cachorro quente'],'A comida precisa ser food'
    return f'Eu estou comendo {comida}'

comida = input('Informe a comida: ')
print(comer_fast_food(comida))


# ALERTA: Cuidado ao utilizar  'assert'