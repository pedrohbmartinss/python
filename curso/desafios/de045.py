import random
computador = random.randint(1,3)
print("""1 - Pedra
2 - Papel
3 - Tesoura""")
opcao = int(input('Escolha uma opção:'))
if computador == 1:
    print('Computador jogou Pedra.')
    if opcao == 2:
        print('Voce jogou Papel - GANHOU')
    elif opcao == 3:
        print('Voce jogou tesoura - PERDEU')
    elif opcao == 1:
        print('Voce jogou pedra - EMPATE')
    else:
        print('Jogada invalida')
elif computador == 2:
    print('Computador jogou Papel')
    if opcao == 2:
        print('Voce jogou Papel - EMPATE')
    elif opcao == 3:
        print('Voce jogou tesoura - GANHOU')
    elif opcao == 1:
        print('Voce jogou pedra - PERDEU')
    else:
        print('Jogada invalida')
elif computador == 3:
    print('Computador jogou tesoura')
    if opcao == 1:
        print('Voce jogou pedra - GANHOU')
    elif opcao == 2:
        print('Voce jogou papel - PERDEU')
    elif opcao == 3:
        print('Voce jogou tesoura - EMPATE')
    else:
        print('Jogada invalida')
else:
    print('Opção invalida')