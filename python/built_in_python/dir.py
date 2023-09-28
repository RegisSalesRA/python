"""
A função dir() em Python é usada para listar os nomes dos atributos e métodos de um objeto. 
Ela retorna uma lista de strings que representam os nomes dos atributos e métodos disponíveis para o objeto. Aqui está um exemplo de como usar dir():
"""

# Criando uma classe simples
class MinhaClasse:
    atributo1 = 10

    def __init__(self):
        self.atributo2 = 20

    def metodo1(self):
        pass

    def metodo2(self):
        pass

# Criando uma instância da classe
objeto = MinhaClasse()

# Usando dir() para listar os atributos e métodos do objeto
lista_de_atributos_e_metodos = dir(objeto)

# Imprimindo a lista
for nome in lista_de_atributos_e_metodos:
    print(nome)
