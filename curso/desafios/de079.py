opcao = ''
numeros = []
while opcao != 'N':
    numeros.append(int(input('Digite um valor: ')))
    if numeros.count(numeros[-1]) == 1:
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
        numeros.pop()
    opcao = input('Quer continuar? [S/N]').upper()
print(f'Você digitou os valores {sorted(numeros)}')
    