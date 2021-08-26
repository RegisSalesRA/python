ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo usuario')
else:
    print('Nao esta logado,por favor checar e-mail')

if ativo or logado:
    print('Bem-vindo usuario')
else:
    print('Nao esta logado,por favor checar e-mail')

if not ativo:
    print('Voce precisa ativar sua conta')
else:
    print('Bem-vindo Usuario')

if ativo is True:
    print('Bem-vindo Usuario')
else:
    print('Voce precisa ativar sua conta')