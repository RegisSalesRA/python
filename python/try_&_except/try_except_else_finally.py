"""
Try / Except / Else / Finally
Dica de quando e onde de tratar codigo:
Toda entrada  do usuario deve ser tratada!
OBS: A funcao do usuario e DESTRUIR seu sistema
# Else => e executado somente se ocorrer o erro
"""


try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'voce digitou {num}')


# Finally
try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('voce nao digitou um valor valido')
else :
    print(f'Voce digitou o numero {num}')
finally:
    print('Executando o finally')
# OBS: o bloco finally sempre e executado independente se ouve execucao ou nao
# O finally geralmente e utilizado para fechar ou desalocar recursos.
# Exemplo mais complexo ERRADO
def dividir(a, b):
    return a / b
num1 = int(input('Informe o primeiro numero: '))



try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numero')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor Incorreto')
# Exemplo mais complexo CORRETO
# OBS: voce e responsavel pelas entradas das suas funcoes.entao,trate-as
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Nao e possivel realizer uma divisao por zero'
num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')
print(dividir(num1, num2))



# Exemplo mais complexo Generico
# OBS: voce e responsavel pelas entradas das suas funcoes.entao,trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Digite um valor correto somente numeros'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))

# Exemplo mais complexo Semi-Generico
# OBS: voce e responsavel pelas entradas das suas funcoes.entao,trate-as

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError,ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro numero: ')
num2 = input('Informe o segundo numero: ')

print(dividir(num1, num2))



# Example New

# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')