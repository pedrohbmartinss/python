matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
maior = 0

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input('Valor: '))
        if matriz[i][c] % 2 == 0:
            par += matriz[i][c]
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
for i in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'{matriz[i][c]}', end= ' ')
print(f'\nA soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna {soma}')
for i in range(0,3):
    if matriz[1][i] > maior:
        maior = matriz[1][i]
print(f'O maior vlor da segunda linha é {maior}')
