"""
Conhecendo o Pickle

A Funcao do pickle e realizar o seguinte processo:

objetivo Python -> BInarizacao

Binarizacao ->  Objeto python

Este processo e chamado de Serializacao/deserializacao

#OBS: O modulo pickle nao e seguro contra dados maliciosos e desta forma nao e recomendado
trabalhar com arquivos pickle vindos de outras pessoas
que voce nao conheca ou de fontes desconhecidas

"""

import pickle

class Animal:
    def __init__(self, nome,):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} esta comendo ...')

class Gato(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.__Animal__nome} esta miando')

felix = Gato('felix')

# Fazendo a escrita em arquivos pickle

with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix),arquivo)