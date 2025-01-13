n = 0
i = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero(999 para parar): '))
    i += 1
    soma += n
print('Voce digitou {} numeros e a soma enetre eles foi {}'.format(i-1, soma-999))