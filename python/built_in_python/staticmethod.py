"""
staticmethod() em Python é um decorador usado para declarar um método de classe como estático.
 Um método estático é um método associado a uma classe em vez de uma instância específica dessa classe. 
 Isso significa que você pode chamar um método estático diretamente na classe, sem a necessidade de criar uma instância da classe.
   Métodos estáticos são frequentemente usados para funcionalidades que pertencem à classe em vez de instâncias individuais.

Aqui está um exemplo de como usar staticmethod() para definir um método estático em uma classe:
"""

class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b

# Chamando métodos estáticos diretamente na classe, sem criar instâncias
resultado_soma = Calculadora.somar(5, 3)
resultado_subtracao = Calculadora.subtrair(10, 4)

print("Soma:", resultado_soma)  # Saída: Soma: 8
print("Subtração:", resultado_subtracao)  # Saída: Subtração: 6
