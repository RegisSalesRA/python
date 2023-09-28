"""

A função eval() em Python é usada para avaliar uma expressão ou código Python em formato de string e retornar o resultado da avaliação. Ela permite que você execute código Python dinamicamente a partir de uma string. No entanto, é importante usar eval() com cautela, pois ele pode executar qualquer código Python e representar um risco de segurança se a entrada não for confiável. Aqui está um exemplo de como usar eval()
"""

# Definindo uma expressão matemática em formato de string
expressao = "2 + 3 * 4"

# Usando eval() para avaliar a expressão
resultado = eval(expressao)

# Imprimindo o resultado
print("Resultado da expressão:", resultado)
