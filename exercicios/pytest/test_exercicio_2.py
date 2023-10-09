
from ..basic.exercicio_2 import lambda_comprimento_palavra



def test_lambda_comprimento_palavra():
    assert lambda_comprimento_palavra(["Palav" ,"Ola", "Jaaaaaan", "Mikasa", "eren"]) == [5, 3, 8, 6, 4]