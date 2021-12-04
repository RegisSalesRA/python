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
        print(f'O alimento {alimento.nome} custa {alimento.preco}$')       

def atualizar_alimentos(lista):
    for alimento in lista:
        print(f'O alimento {alimento.nome} custa {alimento.preco}$')

def atualizar_alimento(lista,item_escolhido):
    print('Lista de Alimentos')
    print('===================')
    print('')
    try:
        for alimento in lista:
            if(item_escolhido == alimento.nome):
                nome: str = input('Informe o novo nome do produto: ')
                preco: float = float(input('Informe o novo preço do produto: '))
                print(alimento.nome)
                alimento.update(nome=nome,preco=preco)
                print(alimento.nome)
    except:
        print('Nao encontrado')