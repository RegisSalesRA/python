def main():
    menu()

def menu():
    print('Enter a choice')
    print('1 somar')
    print('2 subtrair')
    print('3 multiplicar')
    print('4 dividir')
    
    choice = input()
    if(choice == '1'):
        somar()
    elif(choice == '2'):
        print('opcao 2')
    elif(choice == '3'):
        print('opcao 3')
    else:
        print("You entered a wrong choice")


def somar():
    print('valor 1')
    valor_1 = input()
    print('valor 2')
    valor_2 = input()
    
    valor = int(valor_1) + int(valor_2)
    print(valor)


if __name__ == "__main__":
    main()