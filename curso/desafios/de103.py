def jogador(nome = '<desconhecido>' , gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = input('Nome jogador: ')
gols = input('Número de gols: ')

if nome == '':
    jogador(gols = gols)
elif gols == '':
    jogador(nome = nome)
else:
    jogador(nome, gols)
