from views.functions import adicionar_alimento, atualizar_alimento, listar_alimentos
from time import sleep
from typing import List, Dict
from models.alimentos import Alimento

lista_alimentos : List[Alimento] = []

def main():
    menu()

def menu():
    
    print('Selecione alguma opção abaixo: ')
    print('1 - Cadastrar alimento')
    print('2 - Listar alimentos')
    print('3 - Atualizar alimento')
    print('4 - Deletar alimento')
    print('5 - Buscar alimento cadastrado')
    print('6 - Sair do sistema')
    
    choice = input()
    if(choice == '1'):
        adicionar_alimento(lista_alimentos)
        print('')
        sleep(2)
        menu()
    elif(choice == '2'):
        listar_alimentos(lista_alimentos)
        print('')
        print('Digite Menu para voltar ao menu')
        choice = input()
        if(choice == 'Menu'):
            menu()
        else:
            pass    
    elif(choice == '3'):
        print('Digite o nome do alimento que deseja atualizar')
        print('Digite Menu para voltar ao menu')
        choice = input()
        
        if(choice == 'Menu'):
            print('')
            menu()
            print('')
        elif(choice != 'Menu'):
            atualizar_alimento(lista_alimentos,choice)
            print('')
            menu()
        else:
            pass
    elif(choice == '4'):
        print('opcao 4')
    elif(choice == '5'):
        print('opcao 5')
    elif(choice == '6'):
        print('Volte sempre!')
        sleep(2)
        exit(0)    
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


if __name__ == "__main__":
    main()