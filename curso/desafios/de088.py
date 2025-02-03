import random
vezes = int(input('Quantos jogos você quer que eu sorteie?: '))
jogo = []
cont = 0
for i in range(0,vezes):
    while True:
        num = random.randint(1,60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    cont=0
    jogo.sort()
    print(f'Jogo {i}: {jogo}')
    jogo.clear()



