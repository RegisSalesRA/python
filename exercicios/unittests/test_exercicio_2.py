import sys
import unittest

sys.path.append('D:\\python\\')

 
from exercicios.basic.exercicio_2 import lambda_comprimento_palavra 

class Exercicio_1Testes(unittest.TestCase):
        
    def test_values_from_list(self):
        self.assertEqual(lambda_comprimento_palavra(["Palav" ,"Ola", "Jaaaaaan", "Mikasa", "eren"]),[5, 3, 8, 6, 4])


if __name__ == '__main__':
    unittest.main()