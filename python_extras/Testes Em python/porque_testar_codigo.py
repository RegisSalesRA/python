"""
Por que testar nosso codigo?

Testes automatizados!


        APLICACAO WEB
`````````````````````````````
|    frontend - backend     |
|                           |
````````````````````````````
| Testes automatizados      |
`````````````````````````````

Porque testar nosso codigo?
    - Reduzir bugs (problemas) no codigo existente
    - Testes garantem que novos recursos da sua aplicacao nao quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos;
    - Testes garantem que a refatoracao que costumamso a faEr nao tragam novos bugs(problemas);

TDD - Test Driven Development ( Desenvolvimento Guiado por Testes )

Com o TDD e utilizado estagios de desenvolvimento;
    - Voce escreve seu teste primeiro;
    - Entao voce escreve o codigo minimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
    - Entao refatora o codigo para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso e considerado completo;

Estes estagios de desenvolvimento do TDD sao quase como um mantra que os desenvolvedores seguem,conhecidos como:
    - Red;
    - Green;
    - Refactor;
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} esta miando...')


felix = Gato('Felix')
felix.miar()

print(felix.nome)
