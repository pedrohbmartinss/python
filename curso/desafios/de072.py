numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    i = int(input('Digite um numero entre 0 e 10: '))
    if i > 10 or i < 0:
        i = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    else:
        break
print(f'Voce digitou o numero {numeros[i]}')
