numeros = []
par = []
impar = []
for i in range(0,7):
    numeros.append(int(input(f'Digite o {i+1} valor: ')))
    if numeros[0] % 2 == 0:
        par.append(numeros[:])
    else:
        impar.append(numeros[:])
    numeros.clear()
par.sort()
impar.sort()
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores impares digitados foram: {impar}')