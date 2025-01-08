frase = ('Amanda ama pedro').strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('a') + 1))
print('A ultima letra A aparece na posicao {}'.format(frase.rfind('a') + 1))
