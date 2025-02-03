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


