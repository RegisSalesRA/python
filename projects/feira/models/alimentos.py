class Alimento:
    def __init__(self,nome:str,preco:float):
        self.__nome: str= nome
        self.__preco: float = preco

    def update(self,nome,preco):
        self.__nome: str= nome
        self.__preco: float = preco

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco


melancia = Alimento(nome="Melancia 1", preco="12")
laranja = Alimento(nome="Laranja",preco="12")
melao = Alimento(nome="Melao",preco="12")
melao.update(nome="melaozim",preco=12.5)
#print(melao.nome)

lista_alimentos = [melancia,laranja,melao]