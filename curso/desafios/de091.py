from random import randint
from operator import itemgetter
jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
for i, k in jogo.items():
    print(f'{i} tirou {k}')
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, k in enumerate(ranking):
    print(f'{i+1} foi: {k[0]} com {k[1]}')