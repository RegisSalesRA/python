from helpers.helpers import alimento_uppercase
from models.alimentos import Alimento
import os

def adicionar_alimento(lista):
    print('Cadastro de Alimento')
    print('===================')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    
    alimento: Alimento = Alimento(alimento_uppercase(nome), preco)
    lista.append(alimento)

    print(f'O alimento {alimento.nome} foi cadastrado com sucesso!')

def listar_alimentos(lista):
    print('Lista de Alimentos')
    print('===================')
    print('')
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
                alimento.update(nome=alimento_uppercase(nome),preco=preco)
                print(alimento.nome)
    except:
        print('Nao encontrado')

def buscar_alimento(lista,item_escolhido):
    print('Lista de Alimentos')
    print('===================')
    print('')
    try:
        for alimento in lista:
            if(item_escolhido == alimento.nome):
                print(f'O alimento {alimento.nome} esta custando {alimento.preco}')
    except:
        print('Nao encontrado')

def deletar_alimento(lista,choice):
    print('Deletar Alimento')
    print('===================')
    print('')
    try:
        for alimento in lista:
            if(choice == alimento.nome):
                lista.remove(alimento)
                print(f'{alimento} foi deletado com sucesso!')
    except:
        print('Nao encontrado')