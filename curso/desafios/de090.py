aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))

print(f'O nome é igual a {aluno["nome"]}')
print(f'media é igual a {aluno["media"]}')
if aluno['media'] >= 7:
     aluno['situacao'] = 'aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
     aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
print(f'A situação é {aluno["situacao"]}')

