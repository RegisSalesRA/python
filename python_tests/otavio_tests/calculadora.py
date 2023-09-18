def somar(x, y):

    """Soma x e y

    >>> somar(10, 20)
    30
    
    >>> somar(-10, 20)
    10    
    """

    assert isinstance(x,(int,float)), "precisa ser um inteiro mais um float"
    assert isinstance(y,(int,float)), "precisa ser um inteiro mais um float"    
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)