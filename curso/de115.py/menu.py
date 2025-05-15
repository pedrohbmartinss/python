import modulos
arq = 'cursoemvideo.txt'

if not modulos.arquivoexiste(arq):
    modulos.criararquivo(arq)

while True:
    modulos.menu()
    opcao = modulos.verificaint('Sua opção: ')
    if opcao == 1:
        print('-' * 40)
        print('                  PESSOAS CADASTRADAS')
        print('-' * 40)
        modulos.lerarquivo(arq)
        continue
    elif opcao == 2:
        print('-' * 40)
        print('                  CADASTRAR PESSOA')
        print('-' * 40)
        nome = str(input('NOME: '))
        idade = int(input('IDADE: '))
        modulos.cadastrar(arq, nome, idade)
        continue
    else:
        print('-' * 40)
        print('Saindo do sistema... Até logo!')
        print('-' * 40)
        break
 