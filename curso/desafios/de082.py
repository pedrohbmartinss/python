numeros = []
opcao = ''
par = []
impar = []
while opcao != 'N':
    numeros.append(int(input('Digite um valor: ')))
    if numeros[-1] % 2 == 0:
        par.append(numeros[-1])
    else:
        impar.append(numeros[-1])
    opcao = input('Você quer continuar?: [S/N]').upper()
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')