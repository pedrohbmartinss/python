def verifica(n):
    while not n.isnumeric():
        print(f'ERRO, digite um numero!')
        n = input('Digite um numero: ')
    print(f'Voce digitou o numero {n}')


numero = input('Digite um numero: ')
verifica(numero)

