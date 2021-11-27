def somar():
    print('Calcular a soma')
    print('===================')
    
    valor_1: int = int(input('Informe o valor: '))
    valor_2: int = int(input('Informe o valor: '))

    valor = valor_1 + valor_2
    print(valor)

def subtrair():
    print('Calcular a subtracao')
    print('===================')

    valor_1: int = int(input('Informe o valor: '))
    valor_2: int = int(input('Informe o valor: '))
    
    valor = int(valor_1) - int(valor_2)
    print(valor)

def multiplicar():
    print('Calcular a multiplicacao')
    print('===================')

    valor_1: int = int(input('Informe o valor: '))
    valor_2: int = int(input('Informe o valor: '))


    valor = int(valor_1) * int(valor_2)
    print(valor)

def dividir():
    print('Calcular a divisao')
    print('===================')

    valor_1: int = int(input('Informe o valor: '))
    valor_2: int = int(input('Informe o valor: '))
    
    valor = int(valor_1) / int(valor_2)
    print(valor)
