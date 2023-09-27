"""
Definição de Classe e Objeto:
python
Copy code
"""
# Definindo uma classe simples em Python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

"""
Neste exemplo, Pessoa é uma classe que possui dois atributos, nome e idade. Os objetos pessoa1 e pessoa2 são instâncias dessa classe.
"""


# Atributos e Métodos

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando!")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla")
# print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}")
meu_carro.acelerar()

"""
Neste exemplo, marca e modelo são atributos da classe Carro, e acelerar() é um método.
"""

# Encapsulamento em Python

class ContaBancaria:
    def __init__(self, saldo, name):
        self.__saldo = saldo  # Atributo privado
        self._name = None
        # self._name = name   pode passar o valor direto na variavel
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

# Criando um objeto da classe ContaBancaria
conta = ContaBancaria(1000, "Regis")
print("vazio")
print(conta.name)
conta.name = "Regis"
print("nao vazio")
print(conta.name)
print("Saldo:", conta.get_saldo())
conta.depositar(500)
conta.sacar(200)
print("Novo saldo:", conta.get_saldo())

"""
Neste exemplo, o atributo saldo é encapsulado usando o prefixo __, 
tornando-o privado. Métodos get_saldo(), depositar(), e sacar() são usados para acessar e modificar o saldo.
"""


# Herança:


"""
Herança Simples:
A herança simples ocorre quando uma classe (subclasse) herda de uma única classe (superclasse).
"""


class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def fazer_som(self):
        return f"Animal {self.nome} tem a cor {self.cor} e faz latidos"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def fazer_som(self):
        return f"Animal {self.nome} tem a cor {self.cor} e faz miados"
    

rex = Cachorro("Rex", "branco")
whiskers = Gato("Whiskers","Preto")

#print(rex.fazer_som())       # Saída: Au Au!
#print(whiskers.fazer_som())  # Saída: Miau!


"""
Herança multipla
"""

# Classe base 1
class Especie:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        pass

# Classe base 2
class Mamifero:
    def __init__(self, pelos):
        self.pelos = pelos

    def amamentar(self):
        pass

# Classe que herda de ambas as classes base (herança múltipla)
class Cachorro2(Especie, Mamifero):
    def __init__(self, nome, pelos, idade):
        # Chamando os construtores das classes base
        Especie.__init__(self, nome, idade)
        Mamifero.__init__(self, pelos)

    def idade_da_especie(self):
        return f"{self.nome} possui a idade de {self.idade} anos!"

    def falar(self):
        return f"{self.nome} diz Woof!"

    def amamentar(self):
        return f"{self.nome} esta amamentando seus filhotes."

# Criando uma instância de Cachorro
cachorro = Cachorro2("Cachorraum", "Curto", 3)

# Chamando métodos da classe Cachorro
print(cachorro.idade_da_especie()) # possui a idade de 3 anos
print(cachorro.falar())  # Saída: Cachorraum diz Woof!
print(cachorro.amamentar())  # Saída: Rex está amamentando seus filhotes.



"""
Herança multinível 

"""

# Classe base
class AnimalMultinivel:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

# Classe intermediária que herda de Animal
class MamiferoMultinivel(AnimalMultinivel):
    def __init__(self, nome, tipo_pelo):
        super().__init__(nome)
        self.tipo_pelo = tipo_pelo

    def amamentar(self):
        print(f"{self.nome} esta amamentando seu filhote")

# Classe final que herda de Mamifero
class CachorroMultinivel(MamiferoMultinivel):
    def __init__(self, nome, tipo_pelo, idade):
        super().__init__(nome, tipo_pelo)  # Chame super() apenas uma vez aqui
        self.idade = idade

    def fazer_som(self):
        return f"{self.nome} faz som de latidos"

# Instanciando um objeto da classe CachorroMultinivel
cachorro_multinivel = CachorroMultinivel("Cachorro multinivel", "Pelo curto multnivel", "3")
print("")
print(f"Idade: {cachorro_multinivel.idade}")
print(f"Nome: {cachorro_multinivel.nome}")
print(f"Tipo de pelo: {cachorro_multinivel.tipo_pelo}")
cachorro_multinivel.amamentar()
print(f"Som que faz: {cachorro_multinivel.fazer_som()}")


"""
Herança Hibrida
"""


# Classe base
class AnimalHibrida:
    def __init__(self, nome):
        self.nome = 'tartaruga'

    def fazer_som(self):
        pass

# Classe que usa herança simples
class MamiferoHibrida(AnimalHibrida):
    def __init__(self, nome):
        self.nome = nome

    def amamentar(self):
        print(f"{self.nome} esta amamentando seu filhote")

# Classe que usa herança múltipla
class AveHibrida:
    def __init__(self, nome):
        self.nome = nome

    def voar(self):
        print(f"{self.nome} esta voando")

# Classe que combina herança de Mamifero e Ave
class MorcegoHibrida(MamiferoHibrida, AveHibrida):
    def fazer_som(self):
        return f"{self.nome} faz som de chiado"

# Instanciando um objeto da classe Morcego
morcego = MorcegoHibrida("Batemaneiro")

print(f"Nome: {morcego.nome}")
morcego.amamentar()
morcego.voar()
print(f"Som que faz: {morcego.fazer_som()}")

"""
Neste exemplo, Especie é a classe base, e Cachorro e Gato são classes derivadas que herdam de Especie. Cada classe derivada redefine o método fazer_som().
"""

# Polimorfismo

#OBs => isso aqui e referencia da class animal herança simples
def fazer_som(animal):
    return animal.fazer_som()

animal1 = Cachorro("Rex Polimorfismo",'azul' )
animal2 = Gato("Whiskers Polimorfismo", 'verde')

#print(fazer_som(animal1))
#print(fazer_som(animal2))

"""
Neste exemplo, a função fazer_som() pode aceitar objetos de diferentes classes (Cachorro ou Gato) e chamar o método fazer_som() correspondente de cada objeto.
"""

