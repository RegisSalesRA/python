from models.alimentos import Alimento

def adicionar_alimento(lista):
    print('Cadastro de Alimento')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    alimento: Alimento = Alimento(nome, preco)

    lista.append(alimento)

    print(f'O alimento {alimento.nome} foi cadastrado com sucesso!')

def listar_alimentos(lista):
    print('Lista de Alimentos')
    print('===================')
    print('')
    for alimento in lista:
        print(alimento.nome)       