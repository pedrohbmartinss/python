numeros = []
opcao = ''
while opcao != 'N':
    numeros.append(int(input('Digite um valor: ')))
    opcao = input('Você quer continuar?: [S/N]').upper()
numeros.sort(reverse=True)
print(f'Você digitou {len(numeros)} elementos.')
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista')



