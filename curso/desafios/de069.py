adulto = homem = mulher = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    if idade > 18:
        adulto += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    opcao = input('Quer continuar? [S/N] ').upper()
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {adulto}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')