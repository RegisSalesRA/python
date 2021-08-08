from banco import Banco
from clientes import Cliente
from contas import ContaCorrente,ContaPoupanca

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)

if banco.authenticar(cliente1):
    cliente1.conta.depositar(200)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

# print('####################')

# if banco.authenticar(cliente2):
#     cliente2.conta.depositar(0)
#     cliente2.conta.sacar(20)
# else:
#     print('Cliente não autenticado.')

print('####################')

if banco.authenticar(cliente3):
    cliente3.conta.depositar(0)
    cliente3.conta.sacar(21110)
else:
    print('Cliente não autenticado.')

saldo = cliente3.conta.saldo
print(saldo)