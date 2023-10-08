import unittest
import sys
import os

# Obtém o diretório do arquivo atual (onde está seu arquivo de teste)
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Obtém o diretório da pasta que contém o módulo 'exercicio_1.py'
module_dir = os.path.join(current_dir, '..', 'exercicios', 'basic')
print(module_dir)

# Adiciona o diretório ao sys.path para que o Python possa encontrá-lo
sys.path.append('D:\\python\\')
print(module_dir)
 
from exercicios.basic.exercicio_1 import lambda_calcular_media 

class Exercicio_1Testes(unittest.TestCase):
        
    def test_values_from_list(self):
        self.assertEqual(lambda_calcular_media([1,2,3]), 2)


if __name__ == '__main__':
    unittest.main()
