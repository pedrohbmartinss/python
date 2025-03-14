import time
def contagem(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        for i in range(inicio, fim - 1, passo):
            print(f'{i}', end=' ', flush=True)
            time.sleep(0.5)
        print('FIM')
    else:
        for i in range(inicio, fim + 1, passo):
            print(f'{i}', end=' ', flush=True)
            time.sleep(0.5)
        print('FIM')


        
contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contagem(inicio, fim, passo)
