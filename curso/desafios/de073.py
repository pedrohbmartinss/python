times = ('Corinthins', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros colocados são: ')
for i in range(0, 5):
    print(times[i])
print('Os 4 ultimos colocados são: ')
for i in range(-4, 0):
    print(times[i])
print('Os times em ordem alfabetica são: ')
print(sorted(times))
print(f'A chapecoense esta na: {times.index('Chapecoense')+ 1 }')