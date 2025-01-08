import random
import time
pc = random.randint(0,5)
print('-=-' * 20)
print('Tente adivinhar o numero que pensei')
print('-=-' * 20)
player = int(input('Digite o numero:'))
print('PROCESSANDO...')
time.sleep(3)
if player == pc:
    print('Parabéns, você acertou, o numero que pensei foi {}'.format(pc))
else:
    print('Voce errou, o numero em que pensei foi {}'.format(pc))