from sys import path

# import python_def_moule.modulo
from python_def_moule import modulo
from python_def_moule.modulo import *
from python.modules.python_def_moule import soma_do_modulo
from .python_modules import soma_do_modulo

 
# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]
 

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(python_def_moule.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))

# print(variavel)
# print(nova_variavel)