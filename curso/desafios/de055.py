maior = 0
menor = 1000000000000000000000000000000000000000000000
for i in range(0,5):
    peso = float(input('Peso da {}º pessoa: '.format((i+1))))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi de {}kgs'.format(maior))
print('O menor peso foi de {}kgs'.format(menor))
