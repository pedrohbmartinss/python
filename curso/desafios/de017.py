import math
cato = float(input('Digite o tamanho do cateto oposto: '))
cata = float(input('Digite o tamanho do cateto adjacente: '))
print('Cateto oposto: {}, Cateto adjacente: {}, Hipotenusa: {:.2f}'.format(cato, cata, math.hypot(cato, cata)))