"""
POO - Poliformismo

Poli -> Muitas
Morfis -> Formas


"""

class Livro:

    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Representacao do objeto
    def __repr__(self):
        return self.titulo

    # Retorna uma string como valor inves do objeto
    def __str__(self):
        return self.titulo

    #
    def __len__(self):
        return len(self.titulo)

    def __del__(self):
        print('Um objeto foi deletado')

    def __add__(self, other):
        return f'{self} - {other}'

livro1 = Livro('Python rocks','Geek',400)

print(livro1)