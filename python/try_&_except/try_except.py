"""

O block try/except
Utilizamos o bloco try/catch para tratar erros que podem ocorrer no nosso codigo. Previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperaddas
A forma geral mais simples e:
try:
    //execucao problematica
except:
    //o que deve ser feito em caso de problema
# Exemplo 1 - Tratando um erro generico
try:
    geek()
except:
    print('Deu algum erro')

"""

# Tente executar a funcao geek(), caso voce encontre erros,imprima a mensagem de erro.
# Exemplo 2 - Tratando um erro generico

try:
    len(5)
except:
    print('Deu algum erro')

# Tente executar a funcao geek(), caso voce encontre erros,imprima a mensagem de erro.
"""
OBS: tratar erro de forma generica nao e a melhor forma de tratamento de erros , o ideal e sempre
tratar de forma especific
"""

# Exemplo 3 - Tratando um erro espefifico
try:
    len(5)
except NameError:
    print('voce esta utilizando uma funcao inexistente')

# Exemplo 4 - Tratando um erro espefifico
try:
    len(5)
except ValueError:
    print('voce esta utilizando uma funcao inexistente')

# Exemplo 5 - Tratando um erro espefifico
try:
    len(5)
except TypeError as err:
    print(f'A aplicacao gerou um seguinte erro:{err}')


# Exemplo 6 - Tratando um erro espefifico
try:
    geek()
except NameError as erra:
    print(f'Deu NameError:{erra}')
except TypeError as errb:
    print(f'Deu TypeError:{errb}')
except:
    print('Deu um erro diferente')
 

def pega_valor(dicionario,chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome":"Geek"}
print(pega_valor(dic,8))

# Fast example

try:
    value = 1 + "a"
    print(value)

except Exception as e:
    print(f'Error: {e}')
