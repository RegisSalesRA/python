"""
Documentando funcoes com docstrings

Podemos ter acesso a documentacao de uma funcao em python utilizando o metodo/propriedadeEspecial especial __doc__

"""

# Exemplo

def diz_oi():
    """Uma funcao simples que retorna a string oi"""
    return 'Oi'


def exponencial(numero,potencia=2):
    """
    Funcao que retorna por padrao o quadrado de um numero ou numero e potencia informada
    :param numero: numero que desejamos gerar o exponencial
    :param potencia: potencia que queremos gerar o exponencial por padrao e 2
    :return: retorna o exponencial de 'numero' por 'potencia
    """
    return numero ** potencia