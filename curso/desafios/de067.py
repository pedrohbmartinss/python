
while True:
    valor = int(input('Quer ver a tabuada de qual valor?: '))
    if valor < 0:
        break
    for i in range(1, 11):
        print(f'{valor} X {i} = {valor*i}')
    i += 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')