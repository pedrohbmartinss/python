sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo: [M/F]').upper()
    if sexo != 'M' and sexo != 'F':
        print('Voce digitou um sexo invalido.')
print('parabens, Você selecionou um sexo valido.')