from views.functions import somar,dividir,multiplicar,subtrair
from time import sleep


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
        
        subtrair()
        menu()
    elif(choice == '3'):
        
        multiplicar()
        menu()
    elif(choice == '4'):
        
        dividir()
        menu()    
    elif(choice == '5'):
        
        sleep(2)
        exit(0)    
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


if __name__ == "__main__":
    main()