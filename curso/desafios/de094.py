pessoa = {}
opcao = ''
lista = []
cont = 0
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: ').upper()
        if pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
            print('ERRO! Por favor, digite apenas M ou F')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    opcao = input('Quer continuar? [S/N]').upper()
    if opcao == 'N':
        break
print(lista)
media = soma/len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idade é {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa['nome']}', end=' ')
print()

    