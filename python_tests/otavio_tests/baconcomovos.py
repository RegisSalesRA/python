"""
1
2
3
4
5
"""

def bacon_com_ovos(n):
    assert isinstance(n,int), ''

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'
    
    if n % 5 == 0:
        return 'Ovos'


    return 'Passar fome'