velo = int(input('Qual a velocidade do carro?'))
multa = (velo-80)*7
if velo > 80:
    print('MULTADO, sua multa foi de {} reais'.format(multa))
else:
    print('Boa viagem!')
