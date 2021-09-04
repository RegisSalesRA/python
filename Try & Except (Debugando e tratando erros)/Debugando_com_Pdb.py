"""
Debugando com PDB
PDB -> Python Debugger
#OBS: A utilizacao do print() para debugar codigo e uma pratica ruim
def dividir(a,b):
    print(f'a={a},b={b}')
    try:
        return int(a)/int(b)
    except(ValueError,ZeroDivisionError) as err:
        return f'ocorreu um erro em {err}'
print(dividir(8,4))
# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em python,podemos fazer isso em diferentes IDES, como pycharm ou utilizando
# o pdb - python Debugger
def dividir(a,b):
    try:
        return int(a)/int(b)
    except(ValueError,ZeroDivisionError) as err:
        return f'ocorreu um erro em {err}'
print(dividir(8,4))
# Exemplo com o pdb - python debugger
# Para utilizar o python debugger , precisamos importar a bibiloteca PDB e entao utilizar a funcao set_trace()
# comandos basicos do pdb
# l ( listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debuggin)
import pdb
nome = 'Angelica '
sobrenome = 'Jolie '
#pdb.set_trace()
import pdb; pdb.set_trace()
nome_completo = nome + '' + sobrenome
curso = 'programacao em python '
final = nome_completo + 'faz o curso de ' + curso
print(final)
# Porque utilizar este formato?
# o debug e utilizado durante o desenvolvimento . Custamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso ,ao inves de colocarmos o import do pdb no inicio do arquivo
# nos colocamos somente onde vamos debuggar , e ao finalizar ja fazemos a remocao
"""


# Exemplo com o pdb - python debugger 3
# Para utilizar o python debugger , precisamos importar a bibiloteca PDB e entao utilizar a funcao set_trace()
# comandos basicos do pdb
# l ( listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debuggin)


import pdb
nome = 'Angelica '
sobrenome = 'Jolie '
breakpoint()
nome_completo = nome + '' + sobrenome
curso = 'programacao em python '
final = nome_completo + 'faz o curso de ' + curso
print(final)