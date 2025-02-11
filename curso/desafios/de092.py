trabalhador = {}
trabalhador['nome'] = input('Nome: ')
trabalhador['nasce'] = int(input('Ano de nascimento: '))
trabalhador['carta'] = int(input('Carteira de trabalho: '))
if trabalhador['carta'] == 0:
    print(f'Nome tem o valor {trabalhador["nome"]}')
    print(f'Idade tem o valor {trabalhador["nasce"]}')
    print(f'Ctps tem o valor {trabalhador["carta"]}')
else:
    trabalhador['contrato'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = int(input('Salario: R$'))
    print(f'Nome tem o valor {trabalhador["nome"]}')
    print(f'Idade tem o valor {trabalhador["nasce"]}')
    print(f'Ctps tem o valor {trabalhador["carta"]}')
    print(f'Nome tem o valor {trabalhador["contrato"]}')
    print(f'Idade tem o valor {trabalhador["Salário"]}')
    
