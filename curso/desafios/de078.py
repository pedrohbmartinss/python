numeros = []
maior = 0
menor = 0
for i in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
for i, num in enumerate(numeros):
    if num == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições {numeros.index(menor)}')