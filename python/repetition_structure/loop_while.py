numero = 1

while numero <= 10:
    print(numero)
    numero = numero + 1


# EX: 2

resposta = ''

while resposta != 'Sim':
    resposta = input("Acabou já? ")

    
# EX: 3

data = [{ "kanto": [{
      "location" : [
        {
          "Route 4": [
            {
              "pokemon": "Rattata",
              "quantity": 3,
              "time" : "Any",
              "ev_yield": 3,
              "value_status" : "Speed",
              "specification" : "Grass",
              "floor" : ""
            },
            {
              "pokemon": "Spearow",
              "quantity": 3,  
              "time" : "Any",
              "ev_yield": 3,
              "value_status" : "Speed",
              "specification" : "Grass",
              "floor" : ""
            },
            {
              "pokemon": "Goldeen",
              "quantity": 5,
              "time" :"Any",
              "ev_yield" : 5,
              "value_status" : "Attack",
              "specification" : "Water",
              "floor" : ""
            }
          ],
          "Route 5": [
            {
              "pokemon": "Meowth",
              "quantity": 3,
              "time" : "Any",
              "ev_yield": 3,
              "value_status" : "Speed",
              "specification" : "Grass",
              "floor" : ""
            },
            {
              "pokemon": "Mankey",
              "quantity": 3,
              "time" : "Any",
              "ev_yield": 3,
              "value_status" : "Speed",
              "specification" : "Grass",
              "floor" : ""
            }
          ]
        }]}]}]
data_lenght = data[0]["kanto"][0]["location"][0]

data_map = {
    
}
contador = 0
while contador < len(data[0]["kanto"][0]["location"][0]):
    chaves_valor = list(data[0]["kanto"][0]["location"][0].keys())[contador]
    value_key = data[0]["kanto"][0]["location"][0][chaves_valor]
    dataMap = {
        "nome":chaves_valor,
        "extra": ""
    } 
    contador += 1
