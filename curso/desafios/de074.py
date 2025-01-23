import random
maior = 0
c = 0
menor = 9999
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10)
print('Os valores sorteados foram: ')
for i in range(0,5):   
    c = random.randint(0,10)
    print(f'{numeros[c]} ', end='')
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'\nO maior valor foi {maior}')
print(f'O menor valor foi {menor}')

