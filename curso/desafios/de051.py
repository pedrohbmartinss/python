print('='*100)
print('                                     10 TERMOS DE UMA PA')
print('='*100)
inicio = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = inicio + (10 - 1) * razao
for i in range(inicio, decimo + razao, razao):
    print(i, end = ' ')