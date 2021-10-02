"""
Decoradores ( Decoraters )
O que sao decorators??
- Decorators sao funcoes;
- Decoradores envolvem outras funcoes e aprimoram seus comportamentos;
- Decorators tambem sao exemplos de Higher Order Functions;
- Decorators tem uma sintaxe propria usando "@" ( syntact Sugar/ Acuca sintatico )
/--------------------/
/function Decorator/
/------------------/
-------------------
/----------------/
/function Decorada/
/-----------------/
/-----------------/
# Decorators como funcoes ( Sintaxe nao recomendada / Sem acucar Sintatico)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um otimo dia!')
    return sendo()
def saudacao():
    print('Seja bem-vindo ao python !')
# testando 1
# saudacao()
# teste = seja_educado(saudacao)
# teste()
# testando 2
def raiva():
    print('Eu te ODEIO')
raiva_educada = seja_educado(raiva)
raiva_educada()
# Sintaxe com syntax sugar( Acucar sintatico )
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo
@seja_educado_mesmo
def apresentando():
    print('meu nome e pedro')
# Testando
apresentando()
@seja_educado_mesmo
def dormir():
    print('quero dormir...!')
dormir()
#
# |----------------------------------------------
# | HOME | SERVICOES | PRODUTOS | ADMINISTRATIVO |
# -----------------------------------------------
#
# http://www.suaempresa.com.br/home
# http://www.suaempresa.com.br/servicoes
# http://www.suaempresa.com.br/produtos
# http://www.suaempresa.com.br/administrativo
# OBS nao e codigo funcional ( QUE funcione) e apenas exemplo
from django.http import request
from django.shortcuts import redirect
def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')
(obs:isso aqui e uma decoration function)
def home(request):
    return 'Pode acessar home'
def servicoes(request):
    return 'Pode acessar servicoes'
def produtos(request):
    return 'Pode acessar produtos'
@checa_login (isso e um decorator)
def admin(request):
    return 'Pode acessar admin'
"""

# NAO CONFUNDA DECORATOR COM DECORATOR FUNCTION