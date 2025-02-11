dados = []
alunos = []
opcao = ''
cont = 0
media = []
while opcao != 'N':
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    cont += 1
    dados.clear()
    opcao = input('Deseja continuar?: [S/N]').upper()
for i in range(0,cont):
    media.append((alunos[i][1] + alunos[i][2])/2)
print('=-'*20)
print('No.   Nome          Média')
print('-'*28)
for i in range(0,cont):
    print(f'{i:<6}{alunos[i][0]:<15}{media[i]:>.1f}')
print('-'*28)
opcao = ''
while True:
    opcao = int(input('Mostrar notas de qual aluno?: (999 Interrompe)'))
    if opcao == 999:
        break
    print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1:3]}')
    print('-'*28)


