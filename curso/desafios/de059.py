import time
opcao = 999999999999999999999999999999999999
n1 = int(input('Selecione o primeiro numero: '))
n2 = int(input('Selecione o segundo numero: '))
maior = 0
while opcao != 5:
    print("""    1 - Somar
    2 - Multiplicar
    3 - Maior
    4 - Novos numeros
    5 - sair do programa""")
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1,n2,n1 + n2))
    elif opcao == 2:
        print('{} X {} = {}'.format(n1,n2,n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero entre {} e {} é {}'.format(n1,n2, maior))
    elif opcao == 4:
        n1 = int(input('Selecione o primeiro numero: '))
        n2 = int(input('Selecione o segundo numero: '))
    elif opcao == 5:
        print('SAINDO...')
        time.sleep(2)
    else:
        print('Opção invalida, tente novamente.')
print('Programa finalizado')

