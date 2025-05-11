def verificaint(msg):
    while True:
        try:
            n = int(input(msg))
        except:
            print('ERRO: por favor, digite um número inteiro válido')
        else:
            return n


def menu():
    opcao = ''
    print('-' * 40)
    print('                  MENU')
    print('-' * 40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')