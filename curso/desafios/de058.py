import random
computador = random.randint(0, 10)
eu = 0
while eu != computador:
    eu = int(input('Tente acertar o numero que o computador pensou:'))
    if eu != computador:
        print('Você errou, tente novamente.')
print('Voce acertou, o  numero do computador foi {} e o seu foi {}'.format(computador, eu))
