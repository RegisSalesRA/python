"""
POO - Abstracao e encapsulamento

O grande objetivo da POO e encapsula nosso codigo dentro de um grupo logico e hierarquico utilizando
classes

Encapsular -> Capsula

# Relembrando Atributos/Metodos privados em Python

"""

class Conta:

    contador = 500
    def __init__(self,titular,saldo,limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor

# testando
conta1 = Conta('Geek',150,1500)