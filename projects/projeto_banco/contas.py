from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self,agencia,conta,saldo):
        self.agencia =agencia
        self.saldo = saldo
        self.conta= conta
    
    def depositar(self,valor):
        self.saldo += valor
        self.detalhes()
    
    def detalhes(self):
        print(f'Agencia: {self.agencia} '
        f'Conta: {self.conta} '
        f'Saldo: {self.saldo} ')
    @abstractmethod
    def sacar(self,valor):pass

class ContaPoupanca(Conta):
    def sacar(self,valor):
        if valor > self.saldo:
            print('Saldo insuficiente')
        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):

    def __init__(self,agencia,conta,saldo, limite=100):
        super().__init__(agencia,conta,saldo)
        self.limite = limite

    def sacar(self,valor):
            if valor > (self.saldo + self.limite):
                print('Saldo insuficiente')
            self.saldo -= valor
            self.detalhes()

