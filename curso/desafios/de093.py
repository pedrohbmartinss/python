jogador = {}
jogador['nome'] = input('Nome do jogador?: ')
vezes = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
jogador['total'] = 0
gols = []
cont = 0

for i in range(0, vezes):
    gols.append(int(input(f'Quantos gols na partida {i}?: ')))
    cont += 1
    jogador['gols'] = gols.copy()
for i in range(0,vezes):
    jogador['total'] += gols[i]
print('=-'*30)
print(jogador)
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {vezes} partidas.')
for i in range(0, cont):
    print(f'Na partida {i}, fez {gols[i]} gols')