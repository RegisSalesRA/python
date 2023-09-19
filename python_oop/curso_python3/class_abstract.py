from abc import ABC , abstractmethod

class Log(ABC):
    
    @abstractmethod
    def _log(self,msg):
        raise NotImplementedError("Implemente o metodo log")
    
    def log_error(self,msg):
        return self._log(f"Error: {msg}")
    
    def log_success(self,msg):
        return self._log( F"Success: {msg}")
    

class LogPrintMixin(Log):
     def _log(self, msg):
        print(f"{msg} ({self.__class__.__name__})")


l = LogPrintMixin()
l.log_error('Oi')







"""
# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name)
"""
