import modulos
while True:
    modulos.menu()
    opcao = modulos.verificaint('Sua opção: ')
    if opcao == 1:
        print('-' * 40)
        print('                  OPÇÃO 1')
        print('-' * 40)
        continue
    elif opcao == 2:
        print('-' * 40)
        print('                  OPÇÃO 2')
        print('-' * 40)
        continue
    else:
        print('-' * 40)
        print('Saindo do sistema... Até logo!')
        print('-' * 40)
        break
    