class Conta:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def __str__(self):
        return f"Cliente: {self.cliente}, Saldo: {self.saldo:.2f}"


class ContaCorrente(Conta):
    def __init__(self, cliente, saldo_inicial=0, limite_cheque_especial=1000):
        super().__init__(cliente, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def usar_cheque_especial(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor:
            self.saldo -= valor
        else:
            print("Limite de cheque especial excedido!")

    def __str__(self):
        return f"Conta Corrente - {super().__str__()}, Limite Cheque Especial: {self.limite_cheque_especial}"


class ContaPoupanca(Conta):
    def __init__(self, cliente, saldo_inicial=0, taxa_juros=0.03):
        super().__init__(cliente, saldo_inicial)
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        self.saldo += self.saldo * self.taxa_juros

    def __str__(self):
        return f"Conta Poupança - {super().__str__()}, Taxa de Juros: {self.taxa_juros:.2%}"


# Exemplo de uso
cliente1 = "João"
conta_corrente = ContaCorrente(cliente1, 1000)
conta_poupanca = ContaPoupanca(cliente1, 500)

conta_corrente.depositar(500)
conta_poupanca.depositar(300)

conta_corrente.usar_cheque_especial(1500)
conta_poupanca.aplicar_juros()

print(conta_corrente)
print(conta_poupanca)