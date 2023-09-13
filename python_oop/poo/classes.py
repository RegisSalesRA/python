"""
POO - Classes

Em poo , classes nada mais sao que modelos de objetos do mundo real sendo representados computacionalmente

Imagine que voce queira fazer um sistema para automatizar o controle das lampadas da sua casa

Classes pode conter:
    -Atributos -> Representam as caracteristicas do objeto. Ou seja,pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lampada, possivelmente
    iriamos querer saberse a lampadae 110 ou 120 volts,se ela e branca,amarela,vermelha
    outra cor, qual e a luminosidade dela?

    - Metodos (funcoes) Representam os comportamentos do objeto. ou seja, as acoes que este
    objeto pode realizar no sue sistema. No caso da lampada,por exemplo,um comportamento comum que muito
    provavelmente iriamos querer representar no nosso sistema e o de ligar e desligar
    a mesma

Em python para definir  uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra pass em python quando temos um bloco de codigo quando ainda nao esta implementado

OBS: Quando nomeamos uma class em python utulizamos por convencao  nome com inicial
em maisucula  se o nome for composto, utiliza-se as iniciiais de ambas as palavras em maisculo, todas juntas

Dica Geek: em computacao nao usamos : Acentuacao,caracteres especiais,espacoes e similares
para nomes de classe, atributos,metodos,arquivos,diretorios
"""

class Lampada:
    pass

class ContaCorrente:
    pass

lamp = Lampada()
print(type(lamp))
