from views.functions import somar
from time import sleep
from typing import List, Dict


#produtos: List[Produto] = []


def main():
    menu()

def menu():
    print('Enter a choice')
    print('1 somar')
    print('2 subtrair')
    print('3 multiplicar')
    print('4 dividir')
    print('5 sair')
    
    choice = input()
    if(choice == '1'):
        somar()
        menu()
    elif(choice == '2'):
        print('opcao 2')
    elif(choice == '3'):
        print('opcao 3')
    elif(choice == '5'):
        print('Volte sempre!')
        sleep(2)
        exit(0)    
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


if __name__ == "__main__":
    main()