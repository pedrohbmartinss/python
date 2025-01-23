
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o último numero: '))
par = 0
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}º poisção')
for i in numeros:
    if i % 2 == 0:
        par = i
print(f'Os valores pares digitados foram {par}')