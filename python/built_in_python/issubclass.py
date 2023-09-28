"""
A função issubclass() em Python é usada para verificar se uma classe é uma subclasse de outra classe. Ela retorna True se a classe for uma subclasse da classe especificada e False caso contrário. 
A função issubclass() é útil quando você deseja verificar a relação de herança entre classes.
 Aqui está um exemplo de como usar issubclass():
"""

# Definindo uma classe base
class Animal:
    pass

# Definindo uma subclasse de Animal
class Mamifero(Animal):
    pass

# Verificando se Mamifero é uma subclasse de Animal
resultado = issubclass(Mamifero, Animal)
print("Mamifero é uma subclasse de Animal?", resultado)  # Saída: True
