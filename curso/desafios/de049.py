numero = int(input('Digite um numero para ver sua tabuada:'))
for i in range(0,10+1):
    print('{} X {} = {}'.format(numero, i, (numero*i)))
