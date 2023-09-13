"""
POO - O metodo super()

O metodo super() se refere a super classe
"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'Este {self.__nome}  animal fala {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie)
        super().__init__(nome,especie)
        super().faz_som('auauaua')
        self.__raca = raca

felix = Gato('Felix','FElino','Angora')
felix.faz_som('Miau')
print(felix)