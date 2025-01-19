import random
resultado = ' '
i = 0
print('-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-'*20)
while True:
    p1 = int(input('Diga um valor: '))
    opcao = input('Par ou Impar? [P/I]').upper()
    computador = int(random.randint(0,10))
    print('-'*20)
    if opcao == 'P':
        if (computador + p1) % 2 == 0:
            resultado = 'Par'
            print(f'Voce jogou {p1} e o computador {computador}. Total foi {computador + p1} DEU {resultado}')
        else:
            resultado = 'Impar'
            print(f'Voce jogou {p1} e o computador {computador}. Total foi {computador + p1} DEU {resultado}')
    else:
        if (computador + p1) % 2 == 0:
            resultado = 'Par'
            print(f'Voce jogou {p1} e o computador {computador}. Total foi {computador + p1} DEU {resultado}')
        else:
            resultado = 'Impar'
            print(f'Voce jogou {p1} e o computador {computador}. Total foi {computador + p1} DEU {resultado}')
    print('-'*20)
    i += 1
    if resultado[0] != opcao:
        break
print('Voce Perdeu!')
print(f'Voce venceu {i-1} vezes')

