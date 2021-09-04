"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, Ou seja, pelos atributos
nos conseguimos representar computacionamente os estados de um objeto

Em python dividimos os atributos em 3 grupos:
    - Atributos de instancia
    - Atributos de class
    - Atributos dinamicos

# Atributos de instancia: Sao atributos declarados dentro do metodo construtor

# OBS: Metodo contrutor: E um metodo especial utilizado para a construcao do objeto

Em python , por convencao, ficou estabelecido que, todo atributo de classe e publico.
ou seja pode ser acessado por todo o projeto


class Lampada:
    def __init__(self, voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributo privado e publicos
#
#
# class Acesso:
#
#     def __init__(self, nome, email, senha):
#         self.__nome = nome
#         self.__email = email
#         self.__senha = senha

# OBS: lembre-se que isso e apenas uma convencao, ou seja, a linguagem python nao
# vai impedir que facamos acesso aos atributos sinalizados como privados fora de classe

class Acesso:
    def __init__(self,email,senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# exemplo

user = Acesso('user@gmail.com','123456')
print(user.email)
#print(user.__senha) # AtributtError
print(dir(user))

user.mostra_email()
"""

class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation','Video Game', 2300)
p2 = Produto('X-Box','Video Game', 2000)

print(p1.valor) # Acesso possivel mas incorreto de atributo de classe
print(p2.imposto) # incorreto

# Nao precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)
