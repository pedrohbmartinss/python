import random
vezes = int(input('Quantos jogos você quer que eu sorteie?: '))
jogo = [[0], [0], [0], [0], [0], [0]]

print(f'Sorteando {vezes} jogos.')
for i in range(0,6):
    jogo[i] = random.randint(1,60)
for i in range(0, vezes):
    print(f'Jogo {i+1}:', end= ' ')
    print(f'{jogo[i]}')



