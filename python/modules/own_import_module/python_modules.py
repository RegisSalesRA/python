from sys import path

from python.modules.own_import_module.python_def_module import python_def_module, soma_do_modulo
from .python_modules import * 
from .python_modules import soma_do_modulo

 
# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]
 

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(python_def_module.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))

# print(variavel)
# print(nova_variavel)