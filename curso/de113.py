def verificaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor digite um numero valido')
            continue
        else:
            return n



def verificafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor digite um numero valido')
            continue
        else:
            return n


inteiro = verificaint('Digite um numero: ')
print(f'Voce digitou o numero {inteiro}')
float = verificafloat('Digite um numero: ')
print(f'Voce digitou o numero {float}')


