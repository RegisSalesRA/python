"""
A função callable() em Python é usada para verificar se um objeto pode ser chamado (invocado) como uma função.
 Ela retorna True se o objeto for chamável como uma função e False caso contrário. Aqui está um exemplo:
"""

# Definindo uma função simples
def minha_funcao():
    print("Esta é uma função!")

# Definindo uma classe com um método
class MinhaClasse:
    def meu_metodo(self):
        print("Este é um método!")

# Criando objetos da função e da classe
funcao_obj = minha_funcao
objeto_classe = MinhaClasse()

# Verificando se os objetos são chamáveis
chamavel_funcao = callable(funcao_obj)
chamavel_classe = callable(objeto_classe)

# Imprimindo os resultados
print("A função é chamável:", chamavel_funcao)  # Saída: True, porque funcao_obj é uma função
print("A classe é chamável:", chamavel_classe)  # Saída: False, porque objeto_classe não é uma função
