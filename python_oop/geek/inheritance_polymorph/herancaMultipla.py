"""
Poo - Heranca Multipla

#OBS: A heranca multipla pode ser feita de duas maneiras:
    - Por multiderivacao Direta
    - Por Multiderivacao Indireta:
"""

# exemplo 1  - Multidericacao Direta

class Base1:
    pass

class Base2:
    pass

class MultiDerivada(Base1,Base2):
    pass

# Exemplo 2- Multidericavao Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class MultiDerivada1(Base3):
    pass


