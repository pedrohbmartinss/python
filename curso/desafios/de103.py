def jogador(nome = '<desconhecido>' , gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = input('Nome jogador: ')
gols = input('Número de gols: ')

jogador(nome = nome, gols= gols)
