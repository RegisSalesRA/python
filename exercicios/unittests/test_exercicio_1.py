import unittest
import sys

# sys.path.append('C:\\Users\\regis.sales\\Desktop\\projetos\\python>\\')

print(f"CAMINHO {sys.path}")

#from ..exercicios.basic.exercicio_1 import lambda_calcular_media

from exercicios.basic.exercicio_1 import lambda_calcular_media




class Exercicio_1Testes(unittest.TestCase):
        
    def test_values_from_list(self):
        self.assertEqual(lambda_calcular_media([1,2,3]), 5)


if __name__ == '__main__':
    unittest.main()
