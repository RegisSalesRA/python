from dataclasses import dataclass, asdict, astuple, field

@dataclass
class Pessoa:
    name: str
    idade: int
    enderecos: list[str] = field(default_factory=list)

    def nome_completo(self):
        return f'{self.name}  {self.idade}'

if __name__ == '__main__':
    p1 = Pessoa(name="Paw", idade=30)
    print(p1.nome_completo())
    print(asdict(p1))
    print(astuple(p1))