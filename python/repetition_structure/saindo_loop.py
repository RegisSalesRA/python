# EX 1
for numero in range(1,10):
    if numero == 6:
        break
    else:
        print(numero)
print("sai do loop")

# EX 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == "sair":
        break