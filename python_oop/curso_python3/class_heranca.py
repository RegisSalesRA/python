class Pessoa:
    cpf = '1234'
    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print("Nem sai de cliente")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Client(Pessoa):
    def falar_nome_classe(self):
        print("Eita nem sai da classe")
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'blwwwww'


c1 = Client('Regis', 'Sales')
c1.falar_nome_classe()
a1 = Aluno("MAria","Helena")
a1.falar_nome_classe()
print(a1.cpf)