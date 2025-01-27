dados = []
pessoas = []
opcao = ''
maior = 0
menor = 99999
while opcao != 'N':
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    opcao = input('Quer continuar?: [S/N] ').upper()
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end= ' ')
print(f'\nO menor peso foi de {menor}kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end= ' ')


