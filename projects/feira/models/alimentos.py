class Alimento:

    def __init__(self,nome:str,preco:float):
        self.__nome: str= nome
        self.__preco: float = preco

    def update(self,nome,preco):
        self.__nome: str= nome
        self.__preco: float = preco

    def delete(self,object):
        del self.object

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def preco(self) -> float:
        return self.__preco


melancia = Alimento(nome="Melancia 1", preco="12")
laranja = Alimento(nome="Laranja",preco="12")
melao = Alimento(nome="Melao",preco="12")
melao.update(nome="Melao2",preco="12")
#print(melao.nome)

lista_alimentos = [melancia,laranja,melao]
print(f'A lista possui a quantidade de itens {len((lista_alimentos))} atualmente')
choice = "Laranja"

def deletar_alimento(lista,choice):
    print('Deletar Alimento')
    print('===================')
    print('')
    try:
        for alimento in lista:
            if(choice == alimento.nome):
                lista.remove(alimento)
                print('Deletado com sucesso!')
    except:
        print('Nao encontrado')

deletar_alimento(lista_alimentos,choice)
print(f'A lista possui a quantidade de itens {len((lista_alimentos))} atualmente')