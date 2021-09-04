"""
POO -

Objetos - Sao instancias da classe, Ou seja, apos o mapeamento do objeto do mundo real para sua representacao
compoutacional, devemos poder criar quantos objetos forem necessarios, Podempos pensar
nos objetos/instancias de uma classe como variaveis do tipo definindo classe

# Instancia
lamp1 = Lampada('branca',120,60)

lamp1.ligar_desligar()
print(f'A lampada esta desligada? {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000,2000)

usuario = Usuario('angeline','jolie','jolie@gmail.com','123456')


# lamp = Lampada()

nome = 'Agnel'
sobrenome = 'Jolie'
email = 'angel@gmail.com'
senha = '12345'

user = Usuario(nome,sobrenome,email,senha)
print(user)
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo,cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
            print(f'O cliente e {self.__cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

cli = Cliente('Angelica Jolie','123321123')

cc = ContaCorrente(5000,10000,cli)

cc.mostra_cliente()