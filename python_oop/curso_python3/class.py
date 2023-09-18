class Pessoa:
    
    def __init__(self,name,sobrenome):
        self.name = name
        self.sobrenome = sobrenome
    
    def andar(self):
        print(f'{self.name} esta andando...')

p1 = Pessoa("Regis", "Sales")

print(p1.name, p1.sobrenome)
print(p1.sobrenome)

p1.andar()