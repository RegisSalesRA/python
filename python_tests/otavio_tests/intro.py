from calculadora import somar

try:
    print(somar(10, 20))
except AssertionError as e:
    print(f'Conta invalida: {e}')
