matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0,3):
    for c in range(0,3):
        matriz[i][c] = int(input('Digite um valor: '))
for i in range(0,3):
    print()
    for c in range(0,3):
        print(f'{matriz[i][c]}', end=' ')