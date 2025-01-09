soma = 0
velho = 0
nomevelho = ' '
mulher = 0
for i in range(0,4):
    print('-------- {}º PESSOA ----------'.format(i+1))
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Qual o sexo da pessoa?: ')
    soma += idade
    if idade > velho:
        if sexo == 'm':
            velho = idade
            nomevelho = nome
    if idade > 20:
        if sexo == 'f':
            mulher += 1

media = soma/(i+1)
print('A media de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher)
      )

