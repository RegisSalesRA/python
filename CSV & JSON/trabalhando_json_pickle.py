"""
Json and pickle

Json -> Javascript object notation

API - Sao meios de comunicacao entre os servicoes oferecidos por empresas
(twitter, Facebook, Youtube...) e terceiros (nos desenvolvedores)


import json

ret = json.dumps(['produto',{'Playstation 4': ('2tb','Novo','220v')}])
print(type(ret))
print(ret)
"""

import json

class Gato:

    def __init__(self,nome,raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca

felix = Gato('Felix','Vira-Lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)