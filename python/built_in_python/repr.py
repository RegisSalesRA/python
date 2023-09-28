"""


A função repr() em Python é usada para obter a representação de string "reproduzível" de um objeto.
 Essa representação deve ser uma string válida em Python que, idealmente,
   pode ser usada para recriar o objeto original quando passada para a função eval() (embora o uso de eval()
     seja geralmente desencorajado devido a preocupações de segurança).

A função repr() é frequentemente usada para depuração e para fornecer uma representação legível de um objeto que pode ser útil para entender sua estrutura interna.
 Por padrão, muitas classes em Python têm uma implementação de __repr__() que retorna uma representação útil do objeto. 
 No entanto, você também pode substituir o método __repr__() em suas próprias classes personalizadas para fornecer uma representação personalizada.

Aqui está um exemplo de como usar repr():

"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Alice", 30)

# Usando repr() para obter a representação reproduzível
representacao = repr(pessoa)
print(representacao)  # Saída: Pessoa(nome='Alice', idade=30)
